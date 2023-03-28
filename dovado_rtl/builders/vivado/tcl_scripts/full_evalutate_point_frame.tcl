# Output Directory
set outputDir vivado_out/
file mkdir $outputDir

# Design Sources and Constraints
set vhdDir examples/fifo_memory/fifo.vhd
set xdcFile examples/fifo_memory/constraints.xdc
read_vhdl -library bftLib [ glob $vhdDir]
read_verilog [ glob $verilogDir]
read_xdc $xdcFile

# Run synthesis and write checkpoint
synth_design -top fifo_mem -part xc7z020clg400-1 ;# using PYNQ-Z2 as a board (manually imported from file)
# write_checkpoint -force $outputDir/post_synth.dcp
report_timing -no_header -file $outputDir/post_synth_setup_timing.rpt ;# -setup is default behavior
report_utilization -no_primitives -omit_locs -format xml -file $outputDir/post_synth_util.xml

# Optimize and place design; report clock utilization; report timing and utilization estimates;
 # opt_design
 # place_design
# report_clock_utilization -format xml -file $outputDir/clock_util.xml

# if timing violations are present you can run other optimizations
#  if {[get_property SLACK [get_timing_paths -max_paths 1 -nworst 1 -setup]] < 0} {
# puts "Found setup timing violations => running physical optimization"
# phys_opt_design
# }

# write_checkpoint -force $outputDir/post_place.dcp
# report_utilization -format xml -file $outputDir/post_place_util.xml
# report_timing_summary -format xml -file $outputDir/post_place_timing_summary.xml

# Run router, report routing status, timing power and DRC
# route_design
# write_checkpoint -force $outputDir/post_route.dcp
# report_route_status -format xml -file $outputDir/post_route_status.xml
# report_timing_summary -format xml -file $outputDir/post_route_timing_summary.xml
# report_power -format xml -file $outputDir/post_route_power.xml
# report_drc -format xml -file $outputDir/post_imp_drc.xml

# Generate bitstream
# write_bitstream -force $outputDir/cpu.bit
