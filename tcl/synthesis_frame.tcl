# Output Directory
set outputDir ____
file mkdir $outputDir

# Design Sources and Constraints
set vhdlSrc ____
set verilogSrc ____
set xdcFile ____
read_vhdl -library bftLib [ glob $vhdlSrc]
read_verilog [ glob $verilogSrc]
read_xdc $xdcFile

# Run synthesis and write checkpoint
synth_design -top ____ -part ____
write_checkpoint -force $outputDir/post_synth.dcp

report_timing -no_header -file $outputDir/____ ;# -setup is default behavior
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/____
