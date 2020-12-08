# All lines starting with #! may be eventually uncommented on user preference
package require Tcl 8.0
package require struct::set

proc read_all_files { dir libs} {
    set contents [glob -nocomplain -directory $dir *]

    foreach item $contents {
        # recurse - go into the sub directory
        if { [file isdirectory $item] } {
            read_all_files $item $libs
            }
        if { [file extension $item] == ".vhd" } {
            set path [file split  [file normalize $item]]
            set lib [::struct::set intersect $libs $path]
            read_vhdl -library $lib $item
        }
        if { [file extension $item] == ".v" } {
            read_verilog $item
        }
        if { [file extension $item] == ".sv" } {
            read_verilog $item
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
#! read_checkpoint -incremental ____ $outputDir/post_place.dcp ;#here goes directive
place_design ____ ;#here goes directive

# Optimizations in case of timing violations
if {[get_property slack [get_timing_paths -max_paths 1 -nworst 1 -setup]] < 0} {
puts "found setup timing violations => running physical optimization"
phys_opt_design
}

write_checkpoint -force $outputDir/post_place.dcp

#! read_checkpoint -incremental ____ $outputDir/post_route.dcp ;#here goes directive
route_design ____ ;#here goes directive
write_checkpoint -force $outputDir/post_route.dcp

report_timing -no_header -file $outputDir/____
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/____
