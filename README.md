
# Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  * [Adding Custom Processing Steps](#custom-step)
- [Examples](#examples)
  * [Retrieiving Available Metrics](#metrics)
  * [neorv32 (VHDL)](#neorv32)
  * [corundum (VERILOG)](#corundum)
  * [cv32e40p (SYSTEM-VERILOG)](#cv32e40p)
  * [Rocket-chip (CHISEL)](#rocket-chip)
  * [Convolution Filter (HLS)](#convolution)
- [RAW'22 Experiments](#raw-22-experiments)
- [Associated Publication](#associated-publication)

DoVado is a RTL design automation and exploration CLI tool.


<a id="installation"></a>

# Installation
Dovado needs python 3.9 or higher.

``` sh
    pip install dovado-rtl
```


<a id="usage"></a>

# Usage
Dovado takes as input a configuration file which describes different options for automation/exploration.

In the examples directory you can find `configs/template.toml` which describes the general structure of configuration file. On top of this, the example directory hosts `exploration_files/template.toml` and `exploration_files/template.csv` which describe respectively automatic exploration and manual exploration. Exploration files must be referenced by configuration files as specified in the `configs/template.toml` file.

<a id="custom-step"></a>
## Adding Custom Processing Steps
In the examples directory you can find `custom_step.py` which is an example of a custom step added after exploration (e.g. for plot generation after exploration). On top of this, you can find `dovado_work/steps.json`, this file tells dovado which custom step are available and where they are. Finally, we need to specify one or more new flows, this is done through flow files. You can find `dovado_work/extra_vhdl.toml` where there is a new flow specified which adds the custom step after a manual exploration vhdl flow.

To run an example of such flow:

``` sh
  cd examples/
  dovado configs/neorv_extra.toml
```


<a id="examples"></a>

# Examples
All examples can be run from the `examples` folder:

``` sh
    cd examples/
```

<a id="metrics"></a>

## Retrieving Available Metrics
Different boards may have different utilization metrics to use. In general to retrieve them it is sufficient to run your usual config file without the metric section specified. An example of such config file is `examples/configs/get_metrics.toml`.
**WARNING**: retrieving metrics needs manual exploration, the first point specified will be ran to get a test synthesis/implementation.

To test retrieving the metrics:

``` sh
  dovado configs/get_metrics.toml
```

<a id="neorv32"></a>

## neorv32 (VHDL)
[**neorv32**](https://github.com/stnolting/neorv32) is an embedded RISC-V core.

``` sh
    git clone https://github.com/stnolting/neorv32
    cd neorv32/rtl
    mv core/ neorv32/
    mv  neorv32/mem/neorv32_*.default.vhd neorv32/
    rm -r neorv32/mem
    cd ../../
```


Changing the name of the core folder, which contains all vhdl files, to the name of the package which is used along the files is mandatory to make dovado get the project right. On top of this, we delete all `.vhd`  files which are not synthesizable.
Exploring the parameter space of the top module:

``` sh
    dovado configs/neorv_manual.toml
```

An automatic flow is also available for this example:

``` sh
    dovado configs/neorv_automatic.toml
```



<a id="corundum"></a>

## corundum (VERILOG)
[**corundum**](https://ieeexplore.ieee.org/abstract/document/9114811) is an open-source 100Gbps-NIC.

``` sh
    git clone https://github.com/corundum/corundum
    cd corundum/
```


Exploring the parameter space of the top module:

``` sh
  dovado configs/corundum_manual.toml
```


<a id="cv32e40p"></a>

## cv32e40p (SYSTEM-VERILOG)
[**cv32e40p**](https://ieeexplore.ieee.org/document/8106976/) is a low-power RISC-V core.


``` sh
    git clone https://github.com/openhwgroup/cv32e40p
```

Exploring the top module of cv32e40p:
``` sh
  dovado configs/cv32e40p_manual.toml

```


<a id="rocket-chip"></a>
## Rocket-chip (CHISEL)
[**Rocket-chip**](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-17.html) is a chisel RISC-V core.

``` sh
  git clone https://github.com/chipsalliance/rocket-chip
```

Before running the example exploration make sure you have installed all the necessary dependencies to [mapping the rocket core to an FPGA](https://github.com/chipsalliance/rocket-chip#fpga). Then, you can run either a manual or an automatic example:

``` sh
  dovado configs/rocket_chip_manual.toml
  dovado configs/rocket_chip_automatic.toml
```

<a id="convolution"></a>

## Convolution Filter (HLS)
This project is an example HLS project from Xilinx.

``` sh
  git clone https://github.com/Xilinx/Vitis-Tutorials
  mv Vitis-Tutorials/Hardware_Acceleration/Design_Tutorials/01-convolution-tutorial .
```

You can run examples for either manual or automatic exploration:

``` sh
  dovado configs/hls_filter_manual.toml
  dovado configs/hls_filter_automatic.toml
```

<a id="raw22experiments"></a>

# RAW'22 Experiments

We combined Dovado with [Movado](https://github.com/DPaletti/movado) capabilities and run DSEs for different purposes and showcasing Movado approximation capabilities.
We explore [**corundum**](https://ieeexplore.ieee.org/abstract/document/9114811) with the [corresponding section commands](#org9b66d30) .

Then we explore the RISCV extensions of [**neorv32**](https://github.com/stnolting/neorv32), modelling the combination of such extensions with the following **custom metric** (already written in `custom_metrics/extension_score.py`):

```
def extension_score(**kwargs) -> float:
	print("kwargs:")
	print(kwargs)
	return float(__helper_function([int(kwargs["CPU_EXTENSION_RISCV_A"]), int(kwargs["CPU_EXTENSION_RISCV_C"]), int(kwargs["CPU_EXTENSION_RISCV_E"]), int(kwargs["CPU_EXTENSION_RISCV_M"]), int(kwargs["CPU_EXTENSION_RISCV_U"]), int(kwargs["CPU_EXTENSION_RISCV_Zfinx"]), int(kwargs["CPU_EXTENSION_RISCV_Zicsr"]), int(kwargs["CPU_EXTENSION_RISCV_Zifencei"])]))

def __helper_function(variants):
	print(variants)
	return sum(variants) * -1000.00
```

and run with 

    dovado --file-path neorv32/rtl/neorv32/neorv32_ProcessorTop_Minimal.vhd --board xa7a12tcpg238-2I --parameters CPU_EXTENSION_RISCV_A --parameters CPU_EXTENSION_RISCV_C --parameters CPU_EXTENSION_RISCV_E --parameters CPU_EXTENSION_RISCV_M --parameters CPU_EXTENSION_RISCV_U --parameters CPU_EXTENSION_RISCV_Zfinx --parameters CPU_EXTENSION_RISCV_Zicsr --parameters CPU_EXTENSION_RISCV_Zifencei --clock-port clk_i space 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1  --disable-approximate

You will be prompted to choose the objective metrics to optimize, where you will be able to select the custom metric. Please remove the final `--disable-approximate` to run the exact version.


We then explore two DSA for Regular Expressions. We scale up [**TiReX**](https://ieeexplore.ieee.org/abstract/document/8425395) single core with its internal parallelism, but the project is not open-sourced, hence not replicable here. We then scale out [**CICERO**](https://dl.acm.org/doi/abs/10.1145/3476982) engines number according to the [corresponding examples section](#cicero) procedures.

<a id="paper_ref"></a>
# Associated Publication

If you find this repository useful, please use the following citation:

Dovado with custom metrics and Movado:
```
@inproceedings{paletti2021online,
  title={Online Learning RTL Synthesis for Automated Design Space Exploration},
  author={Paletti, Daniele and Peverelli, Francesco and Conficconi, Davide and Santambrogio, Marco D},
  booktitle={2022 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)},
  year={2022},
  organization={IEEE}
}
```

Original Dovado Publication:
```
@inproceedings{paletti2021dovado,
  title={Dovado: An Open-Source Design Space Exploration Framework},
  author={Paletti, Daniele and Conficconi, Davide and Santambrogio, Marco D},
  booktitle={2021 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)},
  pages={128--135},
  year={2021},
  organization={IEEE}
}
```
