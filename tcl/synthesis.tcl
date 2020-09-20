# All lines starting with #! may be eventually stripped on user preference

proc read_all_files { dir } {
    set contents [glob -directory $dir *]

    foreach item $contents {
        # recurse - go into the sub directory
        if { [file isdirectory $item] } {
            read_all_files $item
            }
        if { [file extension $item] == ".vhd" } {
            read_vhdl -library bftLib $item
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
set outputDir vivado_out/
file mkdir $outputDir

# Design Sources and Constraints
set src ./examples/verilog_unsigned_adder/
set xdcFile xdc/constraint.xdc
read_all_files $src
read_xdc $xdcFile

# Run synthesis and write checkpoint
#! read_checkpoint -incremental $outputDir/post_synth.dcp ;# to be turned on for incremental runs (#! is stripped eventually)
synth_design -top krnl_vadd_rtl_adder  -part xc7k70tfbv676-1 -directive default
write_checkpoint -incremental_synth -force $outputDir/post_synth.dcp ;# either -incremental_synth or nothing

report_timing -no_header -file $outputDir/post_synth_setup_timing.rpt ;# -setup is default behavior
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/post_synth_util.xml
