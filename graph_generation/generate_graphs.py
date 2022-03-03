#Script used to generate graphs for Dovado/Movado's output

from datetime import date
from locale import normalize
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.rcsetup as rcsetup
import numpy as np
import pandas as pd
import sys
import getopt
import math
import itertools
import os
import re
import argparse
import traceback
import ndovadomo_charts as ndovado
import movado_charts as mvd
from common_charts import *



def binary_vars_scatter(bin_df, name, title):

    labels = bin_df.columns.values
    x = np.arange(0, len(bin_df.index), 1)
    fig, ax1 = plt.subplots(figsize=(12,4))
    fig.suptitle(title)
    y_height = 1
    lst = ['o', 's', '*', 'v', '^', 'D', 'h', 'x', '+', '8', 'p', '<', '>', 'd', 'H']
    marker = itertools.cycle(lst)
    for l in labels:
        filtered_x = [el for (el,remove) in zip(x, bin_df[l]) if not remove]
        y = [y_height] * len(filtered_x)
        plt.scatter(filtered_x, y, label=l, linewidths=0.5, marker=next(marker))
        y_height = y_height + 1
        
    plt.grid(linestyle='dotted')
    ax1.set_yticks(np.arange(1,len(labels)+1,1), labels=labels)
    ax1.set_xticks(x)

    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '_binary.svg'
    fig.autofmt_xdate()
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

def plot_polar_multidim_space(data_frame, name, title, filter_binary=False):

    #If true plots binary variables in a separate chart
    if filter_binary:
        bdf = split_binary_df(data_frame)
        if(len(bdf.columns.values) > 0):
            binary_vars_scatter(bdf, name, title)

    if len(data_frame.columns.values) < 3:
        return

    fig = plt.figure(figsize=(8, 8))
    fig.suptitle(title, y=1.15)
    labels = data_frame.columns.values
    # print(labels)
    angles = np.arange(0, 2* np.pi, (2*np.pi)/len(labels))
    vdegrees = np.vectorize(math.degrees)
    deg_angles = vdegrees(angles)
    theta = angles
    theta = np.append(theta, theta[0])

    #Take absolute values of data
    data_frame = data_frame.applymap(lambda x: abs(x))
    #Save max and min values of data
    max_col = {}
    min_col = {}
    for l in labels:
        max_col[l] = data_frame[l].max()
        min_col[l] = data_frame[l].min()
    #Normalize data
    data_frame = data_frame.apply(lambda x: x / x.max())


    rect = [0.05, 0.05, 0.95, 0.95]
    axes = [fig.add_axes(rect, projection="polar", label=li) for li in labels]
    axes[0].set_thetagrids(deg_angles, labels=labels, fontsize=10)
    for ax in axes[1:]:
        ax.patch.set_visible(False)
        ax.grid("off")
        ax.xaxis.set_visible(False)

    for ax, angle, label in zip(axes, deg_angles, labels):
        if len(labels)==6:
            magic_value = 6
            label_position = [0, 0.15, 0.3, 0.45, 0.60, 0.75, 1.0]
        elif len(labels)==5:
            magic_value = 6
            label_position = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
        else:
            magic_value = 4
            label_position = [0, 0.25, 0.5, 0.75, 1.0]
        label_value = np.arange(0, max_col[label]+(max_col[label]/magic_value), max_col[label]/magic_value)
        label_value = [round(x,magic_value) for x in label_value]
        label_str = map(str, label_value)

        ax.set_rgrids(label_position, angle=angle, labels=label_str)
        ax.set_rticks(label_position)
        ax.yaxis.grid(visible=False)
        ax.spines["polar"].set_visible(False)
        ax.set_ylim(0, 1)
        if(angle == 0 or angle == 180):
            ax.xaxis.set_tick_params(pad=50)
        else:
            ax.xaxis.set_tick_params(pad=5)

    axes[0].grid(visible=True, which='major', linestyle='dotted')

    n = 0
    for index, row in data_frame.iterrows():
        data_row = list(row)
        data_row.append(row[0])
        axes[0].plot(theta, data_row, linestyle='dashed', label="Solution " + str(n))
        n = n + 1
        axes[0].legend(loc = 'upper right')
    for line in axes[0].get_lines():
        line.set_linewidth('0.75')

    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.autofmt_xdate()
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

def multi_axis_scatter(data_frame, name, title):

    labels = data_frame.columns.values
    fig, ax1 = plt.subplots(figsize=(24,8))
    ax1.set_xlabel("Iterations")
    ax1.set_ylabel("Normalized Exploration Variables")
    fig.suptitle(title)
    rect = [0.05, 0.05, 0.95, 0.95]
    ncols = len(data_frame.index)
    xticks = np.arange(0, ncols, 1)

    #Take absolute values of data
    data_frame = data_frame.applymap(lambda x: abs(x))
    #Save max and min values of data
    max_col = {}
    min_col = {}
    for l in labels:
        max_col[l] = data_frame[l].max()
        min_col[l] = data_frame[l].min()
    #Normalize data
    data_frame = data_frame.apply(lambda x: x / x.max())
    
    lst = ['o', 's', '*', 'v', '^', 'D', 'h', 'x', '+', '8', 'p', '<', '>', 'd', 'H']
    marker = itertools.cycle(lst)
    ranges_labels = []
    for l in labels:
        ranges_labels.append(l+" [" + str(round(min_col[l],4)) + " - " + str(round(max_col[l],4)) + "]")
    for l in labels:
        plt.scatter(xticks, data_frame[l], label=l, linewidths=0.5, marker=next(marker))
    plt.legend(labels=ranges_labels)
    plt.grid(linestyle='dotted')

    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

def multi_boxplot(data_frame, name):

    labels = data_frame.columns.values
    #Take absolute values of data
    data_frame = data_frame.applymap(lambda x: abs(x))
    for label in labels:
        fig, ax1 = plt.subplots(figsize=(6,6))
        fig.suptitle(label + " distribution")
        ax1.boxplot(data_frame[label])
        plt.scatter([1] * len(data_frame.index), data_frame[label], marker='.')
        ax1.set_xlabel(label)
        ax1.xaxis.set_visible(False)
        ax1.grid(visible=True, which='major', linestyle='dotted')
        image_format = 'svg' # e.g .png, .svg, etc.
        image_name = name + label + '.svg'
        fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
        plt.close(fig)


# Plot Dovado graphs as svg images
#

parser = argparse.ArgumentParser(description='Graph generator for Dovado')
parser.add_argument("-d", "--dir", help='dovado out dir', default='./')
parser.add_argument("-r", "--ref_dir", nargs='?', help='reference out dir', default='./')
parser.add_argument("-n", "--normalize_resources",  action='store_true', help='if normalize the data or not')
parser.add_argument("-cic", "--cicero_norm",  action='store_true', help='normalize cicero')
parser.add_argument("-tir", "--tirex_norm",  action='store_true', help='normalize tirex')
parser.add_argument("-hv", "--hypervolume", help='the design name for the list of minimum and maximum <corudundum|neorv|tirex|cicero>', default='corundum')

args = parser.parse_args()

matplotlib.use('svg')
# try:
#     opts, args = getopt.getopt(sys.argv[1:], "d:r:n", [])
# except getopt.GetoptError:
#     print("Use: generate_graphs.py -d <dovado out dir> -r <reference out dir> [-n]")

# normalize_resources = False

# for opt, arg in opts:
#     if opt == "-r":
#         reference_dir_base = arg
#     if opt == "-d":
#         input_dir_base = arg
#     if opt == "-n":
#         normalize_resources = True
input_dir_base = args.dir
reference_dir_base = args.ref_dir
normalize_resources = args.normalize_resources

mins=None
maxs=None
if args.hypervolume=='tirex':
    mins=tirex_mins
    maxs=tirex_maxs
elif args.hypervolume=='cicero':
    mins=cicero_mins
    maxs=cicero_maxs
elif args.hypervolume=='neorv':
    mins=neorv_mins
    maxs=nerov_maxs
elif args.hypervolume=='corundum':
    mins=corundum_mins
    maxs=corundum_maxs
else:
    mins=None
    maxs=None

if not os.path.exists(input_dir_base + "/graphs"):
    os.makedirs(input_dir_base + "/graphs")
input_dir = input_dir_base + "/dovado_work"
output_dir = input_dir_base + "/graphs"

desfr = pd.read_csv(input_dir + '/design_space.csv')
try:
    plot_polar_multidim_space(desfr, output_dir + "/design_space", "Pareto optimal solution parameters", True)
except (ValueError,RuntimeError, TypeError, NameError, KeyError):
    print("Errorrrs plot_polar_multidim_space")
    traceback.print_exc()
try:
    ndovado.single_barchart_multiplot(desfr, output_dir + "/design_bars")
except (ValueError,RuntimeError, TypeError, NameError, KeyError):
    print("Errorrrs single_barchart_multiplot")
    traceback.print_exc()
objfr = pd.read_csv(input_dir + '/objective_space.csv')
#dual_axis_barchart_frequency_res(objfr, output_dir + '/objective_bars')
try:
    ndovado.dual_axis_fused_barchart_frequency_res(objfr, desfr, output_dir + '/objective_bars_single', normalize_resources)
    if args.cicero_norm or args.tirex_norm:
        ndovado.dual_axis_fused_barchart_frequency_res_cicero(objfr, desfr, output_dir + '/objective_bars_single_cicero', normalize_resources,args.tirex_norm)
        ndovado.dual_axis_fused_barchart_frequency_res_third(objfr, desfr, output_dir + '/objective_bars_single_third', normalize_resources,args.tirex_norm)
        ndovado.dual_axis_fused_barchart_frequency_res_separated(objfr, desfr, output_dir + '/objective_bars_objective', output_dir +'/objective_bars_params', normalize_resources,args.tirex_norm)
except (ValueError,RuntimeError, TypeError, NameError, KeyError):
    print("Errorrrs dual_axis_fused_barchart_frequency_res")
    traceback.print_exc()

if mins != None and maxs != None:
    objfr = pd.read_csv(input_dir + '/objective_space.csv')
    try:
        ndovado.dual_axis_fused_barchart_frequency_res_hypervolume(objfr, desfr, output_dir + '/objective_bars_hyperv', normalize_resources,mins, maxs)
        objfr = pd.read_csv(input_dir + '/objective_space.csv')
    except (ValueError,RuntimeError, TypeError, NameError, KeyError):
        print("Errorrrs dual_axis_fused_barchart_frequency_res_hypervolume")
        traceback.print_exc()
try:
    plot_polar_multidim_space(objfr, output_dir + "/objective_space", "Pareto optimal solution objectives")
except (ValueError,RuntimeError, TypeError, NameError, KeyError):
    print("Errorrrs plot_polar_multidim_space")
    traceback.print_exc()
explfr = pd.read_csv(input_dir + '/space_exploration.csv')
try:
    multi_axis_scatter(explfr, output_dir + "/space_exploration", "Normalized exploration iterations")
except (ValueError,RuntimeError, TypeError, NameError, KeyError):
    print("Errorrrs multi_axis_scatter")
    traceback.print_exc()
try: 
    multi_boxplot(explfr, output_dir + "/space_exploration_box_")
except (ValueError,RuntimeError, TypeError, NameError, KeyError):
    print("Errorrrs multi_boxplot")
    traceback.print_exc()

movado_dir = input_dir_base + "/movado_debug"
if os.path.exists(movado_dir):
    reference_dir = reference_dir_base + "/dovado_work"
    print("Generating movado graphs...")
    if not os.path.exists(movado_dir + '/controller_fixed.csv'):
        #Fix controller csv with code below if needed
        with open(movado_dir + '/controller.csv', 'r') as file:
            with open(movado_dir + '/controller_fixed.csv', 'w') as file2:
                data = file.readlines()
                for line in data:
                    regex = re.search("\[([0-9]*),", line)
                    if regex is not None:
                        subst = regex.group(0)[:-1]
                        line = re.sub("\[([0-9]*),",subst, line) 
                    file2.write(line)  
    if not os.path.exists(movado_dir + 'mab_fixed.csv'):
        #Fix mab csv if needed
        with open(movado_dir + '/mab.csv','r') as file:
            with open(movado_dir + '/mab_fixed.csv','w') as file2:
                for cnt, line in enumerate(file):
                    if cnt == 0:
                        line = line.replace(',', ';')
                    else:
                        line = re.sub(r',(?=(((?!\}).)*\{)|[^\{\}]*$)', ';', line)
                    file2.write(line)
    if not os.path.exists(movado_dir + 'mab_weight_fixed.csv'):
        #Fix mab weight csv if needed
        with open(movado_dir + '/mab_weight.csv','r') as file:
            with open(movado_dir + '/mab_weight_fixed.csv','w') as file2:
                for cnt, line in enumerate(file):
                    regex = re.search("\[([0-9]*),", line)
                    if regex is not None:
                        subst = regex.group(0)[:-1]
                        line = re.sub("\[([0-9]*),",subst, line)
                    if cnt == 0:
                        line = line.replace(',', ';')
                    else:
                        line = re.sub(r',(?=(((?!\}).)*\{)|[^\{\}]*$)', ';', line)
                    file2.write(line)

    ctrl = pd.read_csv(movado_dir + '/controller_fixed.csv')
    baseline_expl = pd.read_csv(reference_dir + '/space_exploration.csv') 
    try: 
        mvd.plot_controller_calls(ctrl, baseline_expl, output_dir + "/fitness_calls")
    except (ValueError,RuntimeError, TypeError, NameError, KeyError):
        print("Errorrrs plot_controller_calls")
        traceback.print_exc()
    try: 
        mvd.plot_error(ctrl, output_dir + '/controlller_error')
    except (ValueError,RuntimeError, TypeError, NameError, KeyError):
        traceback.print_exc()
        print("Errorrrs plot_error")
    mab = pd.read_csv(movado_dir + '/mab_fixed.csv', sep=';')
    try: 
        mvd.plot_mean_cost(mab, output_dir + "/mab_cost")
    except (ValueError,RuntimeError, TypeError, NameError, KeyError):
        traceback.print_exc()
        print("Errorrrs plot_mean_cost")
    
    mab_weight = pd.read_csv(movado_dir + '/mab_weight_fixed.csv', sep=';')
    try: 
        mvd.plot_action_weight(mab_weight, output_dir + "/mab_weight")
    except (ValueError,RuntimeError, TypeError, NameError, KeyError):
        traceback.print_exc()
        print("Errorrrs plot_action_weight")
    
