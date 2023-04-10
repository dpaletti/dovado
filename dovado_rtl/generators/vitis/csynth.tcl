# /******************************************
# *MIT License
# *
# *Copyright (c) [2022] [Eleonora D'Arnese, Davide Conficconi, Emanuele Del Sozzo, Luigi Fusco, Donatella Sciuto, Marco Domenico Santambrogio]
# *
# *Permission is hereby granted, free of charge, to any person obtaining a copy
# *of this software and associated documentation files (the "Software"), to deal
# *in the Software without restriction, including without limitation the rights
# *to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# *copies of the Software, and to permit persons to whom the Software is
# *furnished to do so, subject to the following conditions:
# *
# *The above copyright notice and this permission notice shall be included in all
# *copies or substantial portions of the Software.
# *
# *THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# *IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# *FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# *AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# *LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# *OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# *SOFTWARE.
# ******************************************/
#setting the project name
set proj_name      [lindex $argv 2]
#all the input files
set src_dir          [lindex $argv 3]
#target part
set proj_part      [lindex $argv 4]
#target frequency for the csynth step in nanoseconds
set clk      [lindex $argv 5]
#top function (name of the c function that will generate the corresponding hw module)
set toplevel    [lindex $argv 6]
#if any directory to include
set incldirs       [lindex $argv 7]
# current working directory
set cwd [pwd]

puts ""
puts ""
puts ""
puts "***************************************************************"
puts ""
puts "    \[INFO\] HLS project: $proj_name"
puts "    \[INFO\] HLS sources files: $src_dir"
puts "    \[INFO\] Target platform: $proj_part"
puts "    \[INFO\] Clock period: $clk ns"
puts "    \[INFO\] Top level function: $toplevel"
puts "    \[INFO\] Include directories: $incldirs"
puts "    \[INFO\] Current working directory: $cwd"
puts ""
puts "***************************************************************"
puts ""
puts ""
puts ""
puts ""
open_project -reset $proj_name
set_top $toplevel
add_files $src_dir -cflags -I$incldirs
open_solution "solution1"
set_part $proj_part
create_clock -period $clk -name default
csynth_design
export_design -rtl verilog -format ip_catalog
close_project
exit 0
