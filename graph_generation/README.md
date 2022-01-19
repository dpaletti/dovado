## Graph generation for Movado/Dovado

Script to generate data visualization for Dovado/Movado output.
To generate graphs for an exact run of Dovado, or the Dovado output for a Movado run, let <code><dovado_output_folder></code> contain a <code>dovado_work</code> folder:

<code>
python3 generate_graphs.py -d dovado_output_folder [-n]
</code>
  

the <code>-n</code> parameter specifies normalized graphs for the design objectives (used if, for example, we are considering only FPGA utilization of resources, which all range in [0-100%].
 To generate graphs for a Movado run, complete with the comparison with an exact run on the same design, run:
  
<code>
python3 generate_graphs.py -d dovado_approximated_output -r dovado_exact_output [-n]
</code>
  
 where <code>dovado_exact_output</code> was run on the same inputs, including design space and objectives, with the <code>--disable-approximate</code> flag.
