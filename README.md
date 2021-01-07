
# Table of Contents

1.  [Installation](#orgc020a3e)
2.  [Usage](#org4f8647b)
    1.  [Examples](#org12b2aea)
        1.  [neorv32 (VHDL)](#orgd8de369)
        2.  [corundum (VERILOG)](#org43556a3)
        3.  [cv32e40p (SYSTEM-VERILOG)](#org6e54816)

DoVado is a RTL design automation and exploration CLI tool.


<a id="orgc020a3e"></a>

# Installation

DoVado needs python 3.6 or higher. Install it through pip, on many Linux systems use pip3 to force python 3 installation.

    pip3 install --user --no-cache dovado-rtl


<a id="org4f8647b"></a>

# Usage

Dovado has two modes:

-   points: design automation mode in which a file containing parameter values must be given and a file containing all the evaluations is returned for some given metrics,
-   space: design exploration mode in which parameters and their ranges must be given together with some target metrics and the pareto set of design points with respect to the given metrics is returned.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 1:</span> dovado general parameters</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">parameter</th>
<th scope="col" class="org-left">description</th>
<th scope="col" class="org-left">mandatory</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">&#x2013;file-path</td>
<td class="org-left">path to the target file</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">&#x2013;board</td>
<td class="org-left">vivado descriptor of a board</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">&#x2013;parameters</td>
<td class="org-left">parameters to use either for points/space</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">&#x2013;clock-port</td>
<td class="org-left">RTL identifier of the clock port</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">&#x2013;implementation</td>
<td class="org-left">switch to evaluate designs after implementation (default is after synthesis)</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;incremental</td>
<td class="org-left">switch to use incremental synthesis/implementation</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;directives</td>
<td class="org-left">list of directives to pass to synthesis, place and route (default is RuntimeOptimized for all three)</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;target-clock</td>
<td class="org-left">clock (Mhz) to give as a constraint to Vivado (default=1000)</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;metrics</td>
<td class="org-left">list of metrics to target using their integer identifier (default mode is interactive, you will be asked after first synthesis/implementation)</td>
<td class="org-left">no</td>
</tr>
</tbody>
</table>

After those parameters specify points/space both these modes take an argument:

-   points argument: specify the path to the csv file containing the design points to be analyzed. The csv file must contain on each line the value for each of the parameters stated through &#x2013;parameters in the same order,
-   space argument: a list of ranges stated as 1 2 3 4 where this way we would be defining two ranges (1, 2) for the first parameter and (3, 4) for the second parameter

No further parameters can be passed to points

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<caption class="t-above"><span class="table-number">Table 2:</span> dovado space parameters</caption>

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">parameter</th>
<th scope="col" class="org-left">description</th>
<th scope="col" class="org-left">mandatory</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">&#x2013;power-of-2</td>
<td class="org-left">list of &rsquo;y&rsquo; or &rsquo;n&rsquo; where each corresponding parameter, in the same order, is specified as a power of 2 (default is &ldquo;n&rdquo; for all parameters)</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;param-initial-values</td>
<td class="org-left">state parameters which are guaranteed to synthesize/implement in order to retrieve the usage metrics after first synthesis</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;optimization-runtime</td>
<td class="org-left">set as a termination condition a timeout (which will be taken as a hint and not strictly respected) as hh:mm:ss (default is a tolerance based termination criterion)</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;record-design-values</td>
<td class="org-left">record all design values in a csv file</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">&#x2013;read-design-values</td>
<td class="org-left">read design values from a csv file</td>
<td class="org-left">no</td>
</tr>
</tbody>
</table>

Directory structure is vital for the functioning of the tool:

-   VHDL: if a package is used the corresponding folder must be named exactly as the package; if one wants to analyse a module in a project with multiple packages each file belonging to a given package must reside in a subfolder with the same name as the package it belongs to:
    -   package-name (top folder must have the name of the top package if it exists or any name if it does not exist)
        -   file-1 (belonging to package-name)
        -   file-2 (belonging to package-name)
        -   subpackage1-name
            -   file-1 (belonging to subpackage-name)
            -   file-2 (belonging to subpackage-name)
            -   &#x2026;
        -   subpackage2-name
            -   &#x2026;
        -   &#x2026;
-   VERILOG/SYSTEM-VERILOG: include directives are not supported all files must be in the same folder, no subfolders allowed.


<a id="org12b2aea"></a>

## Examples


<a id="orgd8de369"></a>

### neorv32 (VHDL)

    git clone https://github.com/stnolting/neorv32
    cd neorv32/rtl
    mv core neorv32

Changing the name of the core folder, which contains all vhdl files, to the name of the package which is used along the files is mandatory to make dovado get &rsquo;use&rsquo; directives right.
Exploring the parameter space of the top module:

    dovado --file-path <path to "neorv32/rtl/neorv32/neorv32_top.vhd"> --board xc7k70tfbv676-1 --parameters MEM_INT_IMEM_SIZE --parameters MEM_INT_DMEM_SIZE --clock-port clk_i --metrics 0 --metrics 1 --metrics 4 --metrics 9 space 16384 131072 8129 65536 --power-of-2 y --power-of-2 y

Above we are optimizing two memory parameters (MEM<sub>INT</sub><sub>IMEM</sub><sub>SIZE</sub>, MEM<sub>INT</sub><sub>DMEM</sub><sub>SIZE</sub>) with clk<sub>i</sub> as the clock port with metrics chosen:

-   frequency (0)
-   LUT occupation (1)
-   REGISTER occupation (4)
-   BRAM occupation (9)

Ranges are specified after space and we also specify that we want to search only among power of 2&rsquo;s solutions.


<a id="org43556a3"></a>

### corundum (VERILOG)

    git clone https://github.com/corundum/corundum
    cd corundum/

Exploring the parameter space of the top module:

    dovado --file-path <path to "corundum/fpga/common/rtl/cpl_queue_manager.v"> --board xc7k70tfbv676-1 --target-clock 100000 --parameters OP_TABLE_SIZE --parameters QUEUE_INDEX_WIDTH --parameters PIPELINE --clock-port clk --metrics 0 --metrics 1 --metrics 4 --metrics 9 space 8 64 4 11 2 32 --record-design-values


<a id="org6e54816"></a>

### cv32e40p (SYSTEM-VERILOG)

    git clone https://github.com/openhwgroup/cv32e40p
    cd rtl
    mkdir testing
    cp cv32e40p_fifo.sv testing/

In this project an include directory is used but dovado does not currently support it thus we create a subfolder, name may be whatever, where to isolate the module we are interested in studying. This workaround is only possible if the module one wants to study works standalone without include directives.

    dovado --file-path ../../test_projects/cv32e40p/rtl/testing/cv32e40p_fifo.sv --board xc7k70tfbv676-1 --target-clock 100000 --parameters DEPTH --parameters DATA_WIDTH --clock-port clk_i --metrics 0 --metrics 1 --metrics 4 --metrics 9 space 2 4294967296 2 64 --power-of-2 y --power-of-2 y

