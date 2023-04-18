package require Tcl 8.0
package require struct::set

# causes segfault on some machines
# set_param general.maxThreads 8

proc create_file_list { dir} {
    set contents [glob -nocomplain -directory $dir *]
    set subdirs {}
    set files {}
    foreach item $contents {
        if { [file isdirectory $item] } {
            set files [concat $files [create_file_list $item]]
        } else {
            lappend files $item
        }
    }

    return $files
}

proc get_depth string {
    regexp -all / $string
}

proc lmap_depth { in_list} {
    # for some reason Vivado TCL does not recognise lmap as a valid command
    set out {}
    foreach item $in_list {
        lappend out [get_depth $item]
    }
    return $out
}

proc lmap_idx { filenames indices} {
    set out {}
    foreach item $indices {
        lappend out [lindex $filenames $item]
    }
    return $out
}

proc read_all_files { dir libs} {
    set filenames [create_file_list $dir]
    set depths [lmap_depth $filenames]
    set indices [lsort -indices -integer -decreasing $depths]
    set filenames [lmap_idx $filenames $indices]

    foreach item $filenames {
        set path [file split  [file normalize $item]]
        set lib [::struct::set intersect $libs $path]
        puts $path
        if { [file extension $item] == ".vhd" } {
            read_vhdl -vhdl2008 -library $lib $item
        }
        if { [file extension $item] == ".v" } {
            read_verilog -library $lib $item
        }
        if { [file extension $item] == ".sv" } {
            # -library in system verilog files may create issues
            read_verilog -sv $item
        }
    }
}

# Output Directory
set outputDir ____
file mkdir $outputDir

# Design Sources and Constraints
set src ____
set xdcFile ____
set libs_list ____
read_all_files $src $libs_list
____
read_xdc $xdcFile


# Run synthesis and write checkpoint
#! read_checkpoint -incremental $outputDir/post_synth.dcp ;# to be turned on for incremental runs (#! is stripped eventually)
synth_design -top ____  -part ____ -directive ____
write_checkpoint ____ -force $outputDir/post_synth.dcp ;# either -incremental_synth or nothing

# Run implementation
opt_design
#! read_checkpoint -incremental $outputDir/post_place.dcp ;#here goes directive
place_design -directive ____ ;#here goes directive

# Optimizations in case of timing violations
if {[get_property slack [get_timing_paths -max_paths 1 -nworst 1 -setup]] < 0} {
puts "found setup timing violations => running physical optimization"
phys_opt_design
}

write_checkpoint -force $outputDir/post_place.dcp

#! read_checkpoint -incremental $outputDir/post_route.dcp ;#here goes directive
route_design -directive ____ ;#here goes directive
write_checkpoint -force $outputDir/post_route.dcp

report_timing -no_header -file $outputDir/____
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/____
