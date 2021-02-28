# All lines starting with #! may be eventually uncommented on user preference
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
            lappend subdirs $item
        } else {
            lappend files $item
        }
    }

    foreach item $subdirs {
        set contents [glob -nocomplain -directory $item *]
        foreach iitem $contents {
            lappend files $iitem
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
            read_vhdl -library $lib $item
        }
        if { [file extension $item] == ".v" } {
            read_verilog $item
        }
        if { [file extension $item] == ".sv" } {
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

report_timing -no_header -file $outputDir/____ ;# -setup is default behavior
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/____
