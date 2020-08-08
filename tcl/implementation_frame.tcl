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

# Run implementation
opt_design
place_design

# Optimizations in case of timing violations
if {[get_property slack [get_timing_paths -max_paths 1 -nworst 1 -setup]] < 0} {
puts "found setup timing violations => running physical optimization"
phys_opt_design
}

write_checkpoint -force $outputdir/post_place.dcp

route_design
write_checkpoint -force $outputdir/post_route.dcp

report_timing -no_header -file $outputdir/____
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/____
