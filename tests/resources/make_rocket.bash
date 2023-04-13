#!/usr/bin/env sh

make verilog CONFIG=freechips.rocketchip.system.DefaultFPGAConfig -C ../resources/rocket-chip/vsim
mkdir chisel_generated
mv ../resources/rocket-chip/vsim/generated-src/freechips.rocketchip.system.DefaultFPGAConfig/SimDTM.v ../resources/rocket-chip/vsim/generated-src/freechips.rocketchip.system.DefaultFPGAConfig/SimDTM.sv
rm -r chisel_generated/
mv ../resources/rocket-chip/vsim/generated-src chisel_generated/
