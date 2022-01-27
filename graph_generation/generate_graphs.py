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

def shorten_labels(labels):
    shorthand = {'Slice LUTs*' : 'LUTs', 'Slice Registers' : 'FF', 'Block RAM Tile':'BRAM', 'frequency' : 'Freq.', \
    'NCluster': 'NClstr', 'ClusterWidth':'ClstrWdt', 'CLB LUTs*' : 'LUTs', 'CLB Registers' : 'FF', 'instr_mem_size':'$I_AddrSz', \
     'avg_perf_metric':'AVG_Gbps', 'AddressWidthInstr':'$I_AddrSz', 'AddressWidthData':'$D_AddrSz', \
     'BB_N':'#Engn','CC_ID_BITS':'Window','PC_WIDTH':'$I_AddrSz', 'avg_gbps_per_luts': 'Gbps/LUTs', \
     'QUEUE_INDEX_WIDTH':'QUE_IDX_WDT', 'OP_TABLE_SIZE':'OP_TAB_SZ' }
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
    plt.close(fig)


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
    plt.close(fig)

def dual_axis_fused_barchart_frequency_res(data_frame, data_frame_2, name, normalize_res):

    labels_2 = data_frame_2.columns.values   
    labels = data_frame.columns.values 
    data_frame = data_frame.applymap(lambda x: abs(x))
    data_frame_joined = data_frame.join(data_frame_2)
    data_frame_joined = data_frame_joined.sort_values(by=['frequency'])
    data_frame = data_frame_joined.drop(columns=labels_2)
    data_frame_2 = data_frame_joined.drop(columns=labels)

    labels = data_frame.columns.values
    #Take absolute values of data
    data_frame = data_frame.applymap(lambda x: abs(x))
    #Normalize frequency data (0-100) 
    fmax = data_frame['frequency'].max()
    data_frame['frequency'] = data_frame['frequency'].map(lambda x: (x / fmax))
    fig, ax = plt.subplots(2, 1, figsize=(5,5))
    # fig, ax = plt.subplots(2, 1, figsize=(10,5))

    ax2 = ax[0].twinx()
    res_df = data_frame.drop(columns='frequency')
    maxres = max(res_df.max())
    #Normalize resource data
    res_df = res_df.apply(lambda x: x / maxres)
    
    width = 0.2
    # width = 0.08
    x = np.arange(len(data_frame.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        if l == 'frequency':
            ax[0].bar(x+offs[i], data_frame[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
        else:
            ax[0].bar(x+offs[i], res_df[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
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

    ax[0].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(-0.1, 1.25), ncol=len(data_frame.columns))
    # ax[0].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.1, 1.2), ncol=len(data_frame.columns))
    #, bbox_to_anchor=(1.1, 0.5))

    labels = data_frame_2.columns.values
    #ax2 = ax[1].twinx()
    width = 0.2
    # width = 0.08
    x = np.arange(len(data_frame_2.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        ax[1].bar(x+offs[i], data_frame_2[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
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
    #ax[1].legend(shorten_labels(labels),loc='center left', bbox_to_anchor=(1.1, 0.5))
    ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(-0.1, 1.25), ncol=len(data_frame_2.columns))
    # ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.2), ncol=len(data_frame_2.columns))

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)
    fig.savefig(name + '.pdf', format='pdf', bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

def dual_axis_fused_barchart_frequency_res_cicero(data_frame, data_frame_2, name, normalize_res, tirex):

    # labels = data_frame.columns.values    

    data_frame = data_frame.applymap(lambda x: abs(x))
    data_frame = data_frame.sort_values(by=['frequency'])

    hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    matplotlib.rcParams['hatch.linewidth'] = 0.3  # previous pdf hatch linewidth
    #Take absolute values of data
    #Normalize frequency data (0-100) 
    fmax = data_frame['frequency'].max()
    avgperf_max = data_frame['avg_perf_metric'].max()
    data_frame['frequency'] = data_frame['frequency'].map(lambda x: (x / fmax))
    data_frame['instr_mem_size'] = data_frame['instr_mem_size'].map(lambda x: (np.log2(x)))
    isize_max = data_frame['instr_mem_size'].max()

    fig, ax = plt.subplots(3, 1, figsize=(10,8))

    ax2 = ax[0].twinx()
    first_df=data_frame.drop(columns=['instr_mem_size','avg_perf_metric'])
    labels = first_df.columns.values
    res_df = data_frame.drop(columns='frequency')
    if tirex:
        custom_mtrc_df = res_df.drop(columns=['CLB LUTs*','CLB Registers'])
    else:
        custom_mtrc_df = res_df.drop(columns=['CLB LUTs*'])

    res_df_only = res_df.drop(columns=['instr_mem_size','avg_perf_metric'])

    #res_df_only = data_frame.drop(columns='frequency')
    maxres = max(res_df_only.max())
    #Normalize resource data
    res_df_only = res_df_only.apply(lambda x: x / maxres)

    width = 0.25
    x = np.arange(len(data_frame.index))

    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        if l == 'frequency':
            ax[0].bar(x+offs[i], data_frame[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='ooo',zorder=3)
        #elif l == 'instr_mem_size' or l == 'avg_perf_metric':
        #    pass
            #ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='///',zorder=3)
        else:
            ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='xxx',zorder=3)
        i = i + 1
    ax[0].set_xticks(x)
    
    ax[0].margins(x=0.01)
    ax2.margins(x=0.01)

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
    ax[0].grid(visible=True, which='major', linestyle='dotted',axis='y',zorder=0)
    ax2.set_ylabel('Frequency (MHz)')

    ax[0].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=len(first_df.columns))



    custom_mtrc_df_perf = custom_mtrc_df.drop(columns='instr_mem_size')
    labels = custom_mtrc_df.columns.values
    labels = np.flip(labels)
    maxres = max(custom_mtrc_df_perf.max())

    ax2 = ax[1].twinx()
    width = 0.25
    x = np.arange(len(custom_mtrc_df.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    res_df_only = res_df_only.apply(lambda x: x / maxres)

    i = 0
    for l in labels:
        if l == 'instr_mem_size':
            ax[1].bar(x+offs[i], custom_mtrc_df[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='///',zorder=3)
        else:
            ax[1].bar(x+offs[i], custom_mtrc_df_perf[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='///',zorder=3)
        i = i + 1
    ax[1].set_xticks(x)
       
    ax[1].margins(x=0.01)
    ax2.margins(x=0.01)
    ax2.set_yticks(np.linspace(0,1,num=10))
    ax2.set_yticklabels(map(math.floor, np.linspace(0,isize_max,num=10)))
    ax[1].set_yticks(np.linspace(0,avgperf_max,num=10))
    ylabel_vals = np.linspace(0,maxres, num=10)
    ylabel_vals = [round(x,2) for x in ylabel_vals]
    ax[1].set_yticklabels(ylabel_vals)
    if normalize_res:
        ax[1].set_ylabel('Throughput [Gbit/s]')
    else:
        ax[1].set_ylabel('Resources')
        ax[1].plot([0., len(x)], [100/maxres, 100/maxres], "k--")
        labels = np.append('100% Utilization',labels)
    ax[1].grid(visible=True, which='major', linestyle='dotted',axis='y',zorder=0)
    ax2.set_ylabel('$I Size [2**x]')

    ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=len(custom_mtrc_df.columns))

    # labels = data_frame_2.columns.values
    # width = 0.25
    # x = np.arange(len(data_frame_2.index))
    # offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    # i = 0
    # for l in labels:
    #     ax[1].bar(x+offs[i], data_frame_2[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5,zorder=3)
    #     i = i + 1
    # ax[1].set_xticks(x)
    # ax[1].set_yticks(np.arange(0,data_frame_2.max().max(),5))
    # ax[1].set_ylabel('Design Parameters')
    # ax[1].grid(visible=True, which='major', linestyle='dotted',axis='y',zorder=0)
    # ax[1].set_xlabel('Solution')
    # ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.4), ncol=len(data_frame_2.columns))

    # #fig.tight_layout()
    # fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    # fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)

    # custom_mtrc_noinstr_df = custom_mtrc_df.drop(columns='instr_mem_size')
    # labels = custom_mtrc_df.columns.values
    # ax2 = ax[1].twinx()
    # #res_df = data_frame.drop(columns='frequency')
    # maxres = max(custom_mtrc_noinstr_df.max())
    # #Normalize resource data
    # custom_mtrc_noinstr_df = custom_mtrc_noinstr_df.apply(lambda x: x / avgperf_max)
    # custom_mtrc_df['instr_mem_size'] = custom_mtrc_df['instr_mem_size'].map(lambda x: (np.log2(x)))
    
    # width = 0.08
    # x = np.arange(len(custom_mtrc_df.index))
    # offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    # i = 0
    # for l in labels:
    #     if l == 'instr_mem_size':
    #         ax[1].bar(x+offs[i], custom_mtrc_df[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
    #     else:
    #         ax[1].bar(x+offs[i], custom_mtrc_noinstr_df[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
    #     i = i + 1
    # ax[1].set_xticks(x)
    # ax2.set_yticks(np.linspace(0,1,num=10))
    # ax2.set_yticklabels(map(math.floor, np.linspace(0,isize_max,num=10)))
    # ax[1].set_yticks(np.linspace(0,1,num=10))
    # ylabel_vals = np.linspace(0,avgperf_max, num=10)
    # ylabel_vals = [round(x,2) for x in ylabel_vals]
    # ax[1].set_yticklabels(ylabel_vals)
    # if normalize_res:
    #     ax[1].set_ylabel('Resource Utilization (%)')
    # else:
    #     ax[1].set_ylabel('Resources')
    #     ax[1].plot([0., len(x)], [100/avgperf_max, 100/avgperf_max], "k--")
    #     labels = np.append('100% Utilization',labels)
    # ax[1].grid(visible=True, which='major', linestyle='dotted',axis='y')
    # ax2.set_ylabel('Frequency (MHz)')

    # ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.1, 1.4), ncol=len(custom_mtrc_df.columns))



    labels = data_frame_2.columns.values
    width = 0.25
    x = np.arange(len(data_frame_2.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        ax[2].bar(x+offs[i], data_frame_2[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
        i = i + 1
    ax[2].set_xticks(x)
        
    ax[2].margins(x=0.01)
    ax[2].set_yticks(np.arange(0,data_frame_2.max().max(),5))
    ax[2].set_ylabel('Design Parameters')
    ax[2].grid(visible=True, which='major', linestyle='dotted',axis='y')
    ax[2].set_xlabel('Solution')
    ax[2].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=len(data_frame_2.columns))

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    #fig.tight_layout(pad=0.5)
    fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)
    fig.savefig(name + '.pdf', format='pdf', bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

def dual_axis_fused_barchart_frequency_res_third(data_frame, data_frame_2, name, normalize_res, tirex):

    labels_2 = data_frame_2.columns.values   
    labels = data_frame.columns.values 
    data_frame = data_frame.applymap(lambda x: abs(x))
    data_frame_joined = data_frame.join(data_frame_2)
    data_frame_joined = data_frame_joined.sort_values(by=['frequency'])
    idx_names= data_frame_joined[data_frame_joined['CLB LUTs*'] > 100].index
    data_frame_joined.drop(idx_names, inplace=True)
    data_frame_joined = data_frame_joined.applymap(lambda x: abs(x))

    # hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    # matplotlib.rcParams['hatch.linewidth'] = 0.3  # previous pdf hatch linewidth
    #Take absolute values of data
    #Normalize frequency data (0-100) 
    fmax = data_frame['frequency'].max()
    avgperf_max = data_frame['avg_perf_metric'].max()
    data_frame['frequency'] = data_frame['frequency'].map(lambda x: (x / fmax))
    data_frame['instr_mem_size'] = data_frame['instr_mem_size'].map(lambda x: (np.log2(x)))
    isize_max = data_frame['instr_mem_size'].max()

    fig, ax = plt.subplots(2, 1, figsize=(9,5))

    ax2 = ax[0].twinx()
    first_df=data_frame #.drop(columns=['instr_mem_size','avg_perf_metric'])
    labels = first_df.columns.values
    res_df = data_frame.drop(columns='frequency')

    maxres = max(res_df.max())
    res_df_only = res_df.apply(lambda x: x / maxres)

    width = 0.25
    x = np.arange(len(data_frame.index))

    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        if l == 'frequency':
            ax[0].bar(x+offs[i], data_frame[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5,zorder=3)
            # ax[0].bar(x+offs[i], data_frame[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='///',zorder=3)
        elif l == 'instr_mem_size' or l == 'avg_perf_metric':
            ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5,zorder=5)
            # ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='ooo',zorder=3)
        else:
            ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5,zorder=4)
            # ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='xxx',zorder=3)
        i = i + 1
    ax[0].set_xticks(x)
    
    ax[0].margins(x=0.01)
    ax2.margins(x=0.01)

    ax2.set_yticks(np.linspace(0,1,num=10))
    ax2.set_yticklabels(map(math.floor, np.linspace(0,fmax,num=10)))
    ax[0].set_yticks(np.linspace(0,1,num=10))
    ylabel_vals = np.linspace(0,maxres, num=10)
    ylabel_vals = [round(x,2) for x in ylabel_vals]
    ax[0].set_yticklabels(ylabel_vals)
    if normalize_res:
        ax[0].set_ylabel('Resource Utilization (%)\nThroughput [Gb/s]\n2^x $I lines')
    else:
        ax[0].set_ylabel('Resources')
        ax[0].plot([0., len(x)], [100/maxres, 100/maxres], "k--")
        labels = np.append('100% Utilization',labels)
    ax[0].grid(visible=True, which='major', linestyle='dotted',axis='y',zorder=0)
    ax2.set_ylabel('Frequency (MHz)')

    ax[0].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(-0.1, 1.28), ncol=len(labels))


    labels = data_frame_2.columns.values
    width = 0.25
    x = np.arange(len(data_frame_2.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        ax[1].bar(x+offs[i], data_frame_2[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
        i = i + 1
    ax[1].set_xticks(x)
        
    ax[1].margins(x=0.01)
    ax[1].set_yticks(np.arange(0,data_frame_2.max().max(),5))
    ax[1].set_ylabel('Design Parameters')
    ax[1].grid(visible=True, which='major', linestyle='dotted',axis='y')
    ax[1].set_xlabel('Solution')
    ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=len(data_frame_2.columns))

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    #fig.tight_layout(pad=0.5)
    fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)
    fig.savefig(name + '.pdf', format='pdf', bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

def dual_axis_fused_barchart_frequency_res_separated(data_frame, data_frame_2, name, name2,normalize_res, tirex):

    labels_2 = data_frame_2.columns.values   
    labels = data_frame.columns.values 
    data_frame = data_frame.applymap(lambda x: abs(x))
    data_frame_joined = data_frame.join(data_frame_2)
    data_frame_joined = data_frame_joined.sort_values(by=['frequency'])
    idx_names= data_frame_joined[data_frame_joined['CLB LUTs*'] > 100].index
    data_frame_joined.drop(idx_names, inplace=True)
    data_frame_joined = data_frame_joined.applymap(lambda x: abs(x))

    data_frame = data_frame_joined.drop(columns=labels_2)
    data_frame_2 = data_frame_joined.drop(columns=labels)

    # hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    # matplotlib.rcParams['hatch.linewidth'] = 0.3  # previous pdf hatch linewidth
    #Take absolute values of data
    #Normalize frequency data (0-100) 
    fmax = data_frame['frequency'].max()
    avgperf_max = data_frame['avg_perf_metric'].max()
    data_frame['frequency'] = data_frame['frequency'].map(lambda x: (x / fmax))
    data_frame['instr_mem_size'] = data_frame['instr_mem_size'].map(lambda x: (np.log2(x)))
    isize_max = data_frame['instr_mem_size'].max()

    fig, ax = plt.subplots(1, 1, figsize=(11,3))

    ax2 = ax.twinx()
    first_df=data_frame #.drop(columns=['instr_mem_size','avg_perf_metric'])
    labels = first_df.columns.values
    res_df = data_frame.drop(columns='frequency')

    maxres = max(res_df.max())
    res_df_only = res_df.apply(lambda x: x / maxres)

    width = 0.25
    x = np.arange(len(data_frame.index))

    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        if l == 'frequency':
            ax.bar(x+offs[i], data_frame[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5,zorder=3)
            # ax[0].bar(x+offs[i], data_frame[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='///',zorder=3)
        elif l == 'instr_mem_size' or l == 'avg_perf_metric':
            ax.bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5,zorder=3)
            # ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='ooo',zorder=3)
        else:
            ax.bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5,zorder=3)
            # ax[0].bar(x+offs[i], res_df_only[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5, hatch='xxx',zorder=3)
        i = i + 1
    ax.set_xticks(x)
    
    ax.margins(x=0.01)
    ax2.margins(x=0.01)

    ax2.set_yticks(np.linspace(0,1,num=10))
    ax2.set_yticklabels(map(math.floor, np.linspace(0,fmax,num=10)))
    ax.set_yticks(np.linspace(0,1,num=10))
    ylabel_vals = np.linspace(0,maxres, num=10)
    ylabel_vals = [round(x,2) for x in ylabel_vals]
    ax.set_yticklabels(ylabel_vals)
    if normalize_res:
        ax.set_ylabel('Scaled Metrics [%] [Gb/s] [2^x lines]')
    else:
        ax.set_ylabel('Resources')
        ax.plot([0., len(x)], [100/maxres, 100/maxres], "k--")
        labels = np.append('100% Utilization',labels)
    ax.grid(visible=True, which='major', linestyle='dotted',axis='y',zorder=0)
    ax2.set_ylabel('Frequency (MHz)')

    ax.legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.2), ncol=len(labels))
    # fig.tight_layout(rect=[0, 0.0, 1, 1])
    ax.set_xlabel('Solution')

    fig.savefig(name + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)
    fig.savefig(name + '.pdf', format='pdf', bbox_inches = 'tight', dpi=1200)

    fig, ax = plt.subplots(1, 1, figsize=(9,4))

    labels = data_frame_2.columns.values
    width = 0.25
    x = np.arange(len(data_frame_2.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        ax.bar(x+offs[i], data_frame_2[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
        i = i + 1
    ax.set_xticks(x)
        
    ax.margins(x=0.01)
    ax.set_yticks(np.arange(0,data_frame_2.max().max(),5))
    ax.set_ylabel('Design Parameters')
    ax.grid(visible=True, which='major', linestyle='dotted',axis='y')
    ax.set_xlabel('Solution')
    ax.legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=len(data_frame_2.columns))

    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    #fig.tight_layout(pad=0.5)
    fig.savefig(name2 + '.svg', format='svg', bbox_inches = 'tight', dpi=1200)
    fig.savefig(name2 + '.pdf', format='pdf', bbox_inches = 'tight', dpi=1200)

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

movl_fnt = 16
movl_lwdth = 4

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
    ax.legend(fontsize=movl_fnt-2)
    ax.grid(visible=True, which='major', linestyle='dotted')
    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    image_format = 'pdf' # e.g .png, .svg, etc.
    image_name = name + '.pdf'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

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
    image_format = 'pdf' # e.g .png, .svg, etc.
    image_name = name + '.pdf'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

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
    image_format = 'pdf' # e.g .png, .svg, etc.
    image_name = name + '.pdf'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    plt.close(fig)

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
    image_format = 'pdf' # e.g .png, .svg, etc.
    image_name = name + '.pdf'
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

if not os.path.exists(input_dir_base + "/graphs"):
    os.makedirs(input_dir_base + "/graphs")
input_dir = input_dir_base + "/dovado_work"
output_dir = input_dir_base + "/graphs"

desfr = pd.read_csv(input_dir + '/design_space.csv')
try:
    plot_polar_multidim_space(desfr, output_dir + "/design_space", "Pareto optimal solution parameters", True)
except (ValueError,RuntimeError, TypeError, NameError):
    print("Errorrrs plot_polar_multidim_space")
    traceback.print_exc()
try:
    single_barchart_multiplot(desfr, output_dir + "/design_bars")
except (ValueError,RuntimeError, TypeError, NameError):
    print("Errorrrs single_barchart_multiplot")
    traceback.print_exc()
objfr = pd.read_csv(input_dir + '/objective_space.csv')
#dual_axis_barchart_frequency_res(objfr, output_dir + '/objective_bars')
try:
    dual_axis_fused_barchart_frequency_res(objfr, desfr, output_dir + '/objective_bars_single', normalize_resources)
    if args.cicero_norm or args.tirex_norm:
        dual_axis_fused_barchart_frequency_res_cicero(objfr, desfr, output_dir + '/objective_bars_single_cicero', normalize_resources,args.tirex_norm)
        dual_axis_fused_barchart_frequency_res_third(objfr, desfr, output_dir + '/objective_bars_single_third', normalize_resources,args.tirex_norm)
        dual_axis_fused_barchart_frequency_res_separated(objfr, desfr, output_dir + '/objective_bars_objective', output_dir +'/objective_bars_params', normalize_resources,args.tirex_norm)
except (ValueError,RuntimeError, TypeError, NameError):
    print("Errorrrs dual_axis_fused_barchart_frequency_res")
    traceback.print_exc()
try:
    plot_polar_multidim_space(objfr, output_dir + "/objective_space", "Pareto optimal solution objectives")
except (ValueError,RuntimeError, TypeError, NameError):
    print("Errorrrs plot_polar_multidim_space")
    traceback.print_exc()
explfr = pd.read_csv(input_dir + '/space_exploration.csv')
try:
    multi_axis_scatter(explfr, output_dir + "/space_exploration", "Normalized exploration iterations")
except (ValueError,RuntimeError, TypeError, NameError):
    print("Errorrrs multi_axis_scatter")
    traceback.print_exc()
try: 
    multi_boxplot(explfr, output_dir + "/space_exploration_box_")
except (ValueError,RuntimeError, TypeError, NameError):
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
        plot_controller_calls(ctrl, baseline_expl, output_dir + "/fitness_calls")
    except (ValueError,RuntimeError, TypeError, NameError):
        print("Errorrrs plot_controller_calls")
        traceback.print_exc()
    try: 
        plot_error(ctrl, output_dir + '/controlller_error')
    except (ValueError,RuntimeError, TypeError, NameError):
        traceback.print_exc()
        print("Errorrrs plot_error")
    mab = pd.read_csv(movado_dir + '/mab_fixed.csv', sep=';')
    try: 
        plot_mean_cost(mab, output_dir + "/mab_cost")
    except (ValueError,RuntimeError, TypeError, NameError):
        traceback.print_exc()
        print("Errorrrs plot_mean_cost")
    
    mab_weight = pd.read_csv(movado_dir + '/mab_weight_fixed.csv', sep=';')
    try: 
        plot_action_weight(mab_weight, output_dir + "/mab_weight")
    except (ValueError,RuntimeError, TypeError, NameError):
        traceback.print_exc()
        print("Errorrrs plot_action_weight")
    
