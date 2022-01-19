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

colors = ['#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8']

def split_binary_df(data_frame):
    labels = data_frame.columns.values
    c = data_frame.columns[data_frame.isin([0,1]).all()]
    bindf = data_frame[c].copy()
    data_frame.drop(columns=c, axis=1, inplace=True)
    return bindf

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
        label_value = np.arange(0, max_col[label]+(max_col[label]/4), max_col[label]/4)
        label_value = [round(x,4) for x in label_value]
        label_str = map(str, label_value)
        label_position = [0, 0.25, 0.5, 0.75, 1.0]
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

def shorten_labels(labels):
    shorthand = {'Slice LUTs*' : 'LUTs', 'Slice Registers' : 'FF', 'Block RAM Tile':'BRAM', 'frequency' : 'Freq.'}
    nlbl = []
    for l in labels:
        if l in shorthand:
            nlbl.append(shorthand[l])
        else:
            nlbl.append(l)
    return nlbl

def single_barchart_multiplot(data_frame, name):
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    labels = data_frame.columns.values
    #Take absolute values of data
    data_frame = data_frame.applymap(lambda x: abs(x))

    xfigs = 2
    yfigs = math.ceil(len(data_frame.index)/xfigs)
    fig, axs = plt.subplots(xfigs, yfigs, figsize=(18,4))
    nfigs = xfigs * yfigs
    for i in np.arange(0,nfigs):
        iidx = math.floor(i/yfigs)
        jidx = i % yfigs
        if i >= len(data_frame.index):
            fig.delaxes(axs[iidx][jidx])
            continue
        
        width = 0.3
        x = np.arange(len(labels))
        values = list(data_frame.iloc[i])

        axs[iidx][jidx].bar(x, values, width=width, color=colors)
        axs[iidx][jidx].set_xticks(x, rotation=45)
        axs[iidx][jidx].set_xticklabels(labels, rotation=15, fontsize=8)
        #axs[iidx][jidx].set_yticks(np.arange(0,1+0.1,0.1))
        #ylabel_vals = np.arange(0,maxres+maxres/10,maxres/10)
        #ylabel_vals = [round(x,2) for x in ylabel_vals]
        #axs[iidx][jidx].set_yticklabels(ylabel_vals)
        axs[iidx][jidx].set_ylabel('Design Parameters')
        axs[iidx][jidx].grid(visible=True, which='major', linestyle='dotted',axis='y')
        #ax2.set_ylabel('Frequency (MHz)')

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)


def dual_axis_barchart_frequency_res(data_frame, name):

    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    labels = data_frame.columns.values
    #Take absolute values of data
    data_frame = data_frame.applymap(lambda x: abs(x))

    #Normalize frequency data (0-100) 
    fmax = data_frame['frequency'].max()
    data_frame['frequency'] = data_frame['frequency'].map(lambda x: (x / fmax))

    xfigs = 2
    yfigs = math.ceil(len(data_frame.index)/xfigs)
    #fig, axs = plt.subplots(xfigs, yfigs, figsize=(18,4))
    fig, axs = plt.subplots(xfigs, yfigs, figsize=(22,4))
    nfigs = xfigs * yfigs
    for i in np.arange(0,nfigs):
        iidx = math.floor(i/yfigs)
        jidx = i % yfigs
        if i >= len(data_frame.index):
            fig.delaxes(axs[iidx][jidx])
            continue
        ax2 = axs[iidx][jidx].twinx()
        res_df = data_frame.drop(columns='frequency')
        maxres = max(res_df.iloc[i])
        #Normalize resource data
        res_df = res_df.apply(lambda x: x / maxres)
        
        width = 0.3
        x = np.arange(len(labels))
        values = list(res_df.iloc[i])
        values.append(data_frame['frequency'][i])
        axs[iidx][jidx].bar(x, values, width=width, color=colors)
        axs[iidx][jidx].set_xticks(x)
        axs[iidx][jidx].set_xticklabels(shorten_labels(labels))
        ax2.set_yticks(np.arange(0,1+0.1,0.1))
        ax2.set_yticklabels(np.arange(0,fmax+10,fmax/10))
        axs[iidx][jidx].set_yticks(np.arange(0,1+0.1,0.1))
        ylabel_vals = np.arange(0,maxres+maxres/10,maxres/10)
        ylabel_vals = [round(x,2) for x in ylabel_vals]
        axs[iidx][jidx].set_yticklabels(ylabel_vals)
        axs[iidx][jidx].set_ylabel('Resource Utilization (%)')
        axs[iidx][jidx].grid(visible=True, which='major', linestyle='dotted',axis='y')
        ax2.set_ylabel('Frequency (MHz)')

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)

def dual_axis_fused_barchart_frequency_res(data_frame, data_frame_2, name, normalize_res):

    labels = data_frame.columns.values
    #Take absolute values of data
    data_frame = data_frame.applymap(lambda x: abs(x))

    #Normalize frequency data (0-100) 
    fmax = data_frame['frequency'].max()
    data_frame['frequency'] = data_frame['frequency'].map(lambda x: (x / fmax))

    fig, ax = plt.subplots(2, 1, figsize=(12,4))

    ax2 = ax[0].twinx()
    res_df = data_frame.drop(columns='frequency')
    maxres = max(res_df.max())
    #Normalize resource data
    res_df = res_df.apply(lambda x: x / maxres)
    
    width = 0.1
    x = np.arange(len(data_frame.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        if l == 'frequency':
            ax[0].bar(x+offs[i], data_frame[l], width=width, color=colors[i])
        else:
            ax[0].bar(x+offs[i], res_df[l], width=width, color=colors[i])
        i = i + 1
    ax[0].set_xticks(x)
    ax2.set_yticks(np.linspace(0,1,num=10))
    ax2.set_yticklabels(map(math.floor, np.linspace(0,fmax,num=10)))
    ax[0].set_yticks(np.linspace(0,1,num=10))
    ylabel_vals = np.linspace(0,maxres, num=10)
    ylabel_vals = [round(x,2) for x in ylabel_vals]
    ax[0].set_yticklabels(ylabel_vals)
    if normalize_res:
        ax[0].set_ylabel('Resource Utilization (%)')
    else:
        ax[0].set_ylabel('Resources')
        ax[0].plot([0., len(x)], [100/maxres, 100/maxres], "k--")
        labels = np.append('100% Utilization',labels)
    ax[0].grid(visible=True, which='major', linestyle='dotted',axis='y')
    ax2.set_ylabel('Frequency (MHz)')

    ax[0].legend(shorten_labels(labels),loc='center left', bbox_to_anchor=(1.1, 0.5))

    labels = data_frame_2.columns.values
    #ax2 = ax[1].twinx()
    width = 0.1
    x = np.arange(len(data_frame_2.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        ax[1].bar(x+offs[i], data_frame_2[l], width=width, color=colors[i])
        i = i + 1
    ax[1].set_xticks(x)
    #ax.set_xticklabels(shorten_labels(labels))
    #ax2.set_yticks(np.arange(0,1+0.1,0.1))
    #ax2.set_yticklabels(map(math.floor, np.arange(0,fmax+10,fmax/10)))
    #ax[1].set_yticks(np.arange(0,1+0.1,0.1))
    #ylabel_vals = np.arange(0,maxres+maxres/10,maxres/10)
    #ylabel_vals = [round(x,2) for x in ylabel_vals]
    ax[1].set_yticks(np.arange(0,data_frame_2.max().max(),5))
    ax[1].set_ylabel('Design Parameters')
    ax[1].grid(visible=True, which='major', linestyle='dotted',axis='y')
    ax[1].set_xlabel('Solution')
    ax[1].legend(shorten_labels(labels),loc='center left', bbox_to_anchor=(1.1, 0.5))
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)

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

movl_fnt = 14
movl_lwdth = 2.5

def plot_controller_calls(controller, base_space, name):

    exact_calls = []
    estimated_calls = []
    for el in controller[' Exact_Estimated_Calls']:
        elements = el[2:-1].split(' ')
        elements =  [int(x) for x in elements]
        exact_calls.append(elements[0])
        estimated_calls.append(elements[1])
    num_steps = len(controller.index)
    steps = np.arange(0, num_steps)
    fig, ax = plt.subplots()
    ax.plot(steps, exact_calls, label="Exact calls", color=colors[1], linewidth=movl_lwdth)
    ax.plot(steps, estimated_calls, label="Estimated calls", color=colors[2], linewidth=movl_lwdth)
    exact = np.arange(0,len(base_space.index))
    ax.plot(exact, exact, label="No approximator run", color=colors[3], linewidth=movl_lwdth)
    #ax.plot([0,num_steps],[len(base_space.index),len(base_space.index)], color='k', linestyle='dashed', linewidth=0.5)
    ax.set_xlabel("Optimization Steps", fontsize=movl_fnt)
    ax.set_ylabel("Calls to Fitness Function", fontsize=movl_fnt)
    ax.legend()
    ax.grid(visible=True, which='major', linestyle='dotted')
    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)

def plot_error(controller, name):

    fig, ax = plt.subplots()
    num_calls = len(controller.index)
    x = np.arange(0, num_calls, 1)
    y = controller[' Error']
    ax.plot(x[1:], y[1:], label='Error', color=colors[3], linewidth=movl_lwdth)
    ax.set_xlabel('Optimization Steps', fontsize=movl_fnt)
    ax.set_ylabel('RMSE', fontsize=movl_fnt)
    #ax.legend()
    ax.grid(visible=True, which='major', linestyle='dotted')
    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)

def plot_mean_cost(mabdf, name):

    #Take absolute values of data   
    mabdf[' Mean Cost'] = mabdf[' Mean Cost'].map(lambda x: abs(x))

    fig, ax = plt.subplots()
    num_calls = len(mabdf.index)
    x = np.arange(0, num_calls, 1)
    y = mabdf[' Mean Cost']
    ax.plot(x, y, label='Mean Cost', color=colors[2])
    ax.set_xlabel('Optimization Steps', fontsize=movl_fnt)
    ax.set_ylabel('Mean Cost', fontsize=movl_fnt)
    #ax.legend()
    ax.grid(visible=True, which='major', linestyle='dotted')
    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)

def plot_action_weight(mabwdf, name):

    fig, ax = plt.subplots()
    num_calls = len(mabwdf.index)
    x = np.arange(0, num_calls, 1)
    y = mabwdf[' Action']
    coef = np.polyfit(x,y,6)
    poly1d_fn = np.poly1d(coef)
    ax.plot(x, y, color=colors[1], label="Weight value")
    ax.plot(x, poly1d_fn(x), color=colors[3], label="Trend", linewidth=movl_lwdth)
    ax.set_xlabel('Optimization Steps', fontsize=movl_fnt)
    ax.set_ylabel('Time weight', fontsize=movl_fnt)
    ax.legend()
    ax.grid(visible=True, which='major', linestyle='dotted')
    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200) 
# Plot Dovado graphs as svg images
#
matplotlib.use('svg')
try:
    opts, args = getopt.getopt(sys.argv[1:], "d:r:n", [])
except getopt.GetoptError:
    print("Use: generate_graphs.py -d <dovado out dir> -r <reference out dir> [-n]")

normalize_resources = False

for opt, arg in opts:
    if opt == "-r":
        reference_dir_base = arg
    if opt == "-d":
        input_dir_base = arg
    if opt == "-n":
        normalize_resources = True

if not os.path.exists(input_dir_base + "/graphs"):
    os.makedirs(input_dir_base + "/graphs")
input_dir = input_dir_base + "/dovado_work"
output_dir = input_dir_base + "/graphs"

desfr = pd.read_csv(input_dir + '/design_space.csv')
plot_polar_multidim_space(desfr, output_dir + "/design_space", "Pareto optimal solution parameters", True)
single_barchart_multiplot(desfr, output_dir + "/design_bars")
objfr = pd.read_csv(input_dir + '/objective_space.csv')
#dual_axis_barchart_frequency_res(objfr, output_dir + '/objective_bars')
dual_axis_fused_barchart_frequency_res(objfr, desfr, output_dir + '/objective_bars_single', normalize_resources)
plot_polar_multidim_space(objfr, output_dir + "/objective_space", "Pareto optimal solution objectives")
explfr = pd.read_csv(input_dir + '/space_exploration.csv')
multi_axis_scatter(explfr, output_dir + "/space_exploration", "Normalized exploration iterations")
multi_boxplot(explfr, output_dir + "/space_exploration_box_")

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
    plot_controller_calls(ctrl, baseline_expl, output_dir + "/fitness_calls")
    plot_error(ctrl, output_dir + '/controlller_error')
    mab = pd.read_csv(movado_dir + '/mab_fixed.csv', sep=';')
    plot_mean_cost(mab, output_dir + "/mab_cost")
    mab_weight = pd.read_csv(movado_dir + '/mab_weight_fixed.csv', sep=';')
    plot_action_weight(mab_weight, output_dir + "/mab_weight")
