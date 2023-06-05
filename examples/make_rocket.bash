#!/usr/bin/env sh

make verilog CONFIG=freechips.rocketchip.system.DefaultFPGAConfig -C ../rocket-chip/vsim
mv ../rocket-chip/vsim/generated-src/freechips.rocketchip.system.DefaultFPGAConfig/SimDTM.v ../rocket-chip/vsim/generated-src/freechips.rocketchip.system.DefaultFPGAConfig/SimDTM.sv
mkdir -p chisel_generated # ensures the directory exists so that rm does not throw any error
rm -r chisel_generated/ # avoids non-empty target error in move
mv ../rocket-chip/vsim/generated-src chisel_generated/
