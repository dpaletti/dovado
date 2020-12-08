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
set outputDir dovado_work/
file mkdir $outputDir

# Design Sources and Constraints
set src ../neorv32/rtl/neorv32
set xdcFile dovado_work/constraint.xdc
set libs_list { neorv32 }
read_all_files $src $libs_list
read_vhdl -library neorv32 dovado_work/box.vhd
read_xdc $xdcFile

# Run synthesis and write checkpoint
#! read_checkpoint -incremental $outputDir/post_synth.dcp ;# to be turned on for incremental runs (#! is stripped eventually)
synth_design -top box  -part xc7k70tfbv676-1 -directive default
write_checkpoint -incremental_synth -force $outputDir/post_synth.dcp ;# either -incremental_synth or nothing

report_timing -no_header -file $outputDir/post_synth_setup_timing.rpt ;# -setup is default behavior
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/post_synth_util.xml
