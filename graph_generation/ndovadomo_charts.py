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
import compute_hypervolume as chyv
from common_charts import *

ndovadomo_fnt=26
ndovadomo_leg_fonts=20
ndovadomo_tick_lbls=18

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
        ax[0].set_ylabel('Scaled Metrics')
        # ax[0].set_ylabel('Resource Utilization (%)\nThroughput [Gb/s]\n2^x $I lines')
    else:
        ax[0].set_ylabel('Resources')
        ax[0].plot([0., len(x)], [100/maxres, 100/maxres], "k--")
        labels = np.append('100% Utilization',labels)
    ax[0].grid(visible=True, which='major', linestyle='dotted',axis='y',zorder=0)
    ax2.set_ylabel('Frequency (MHz)')

    ax[0].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=len(labels))


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

def dual_axis_fused_barchart_frequency_res_hypervolume(data_frame, data_frame_2, name, normalize_res, mins, maxs):


    new_df = data_frame.copy()
    #print(data_frame)
    data_frame = data_frame.applymap(lambda x: abs(x))
    avgperf_max = data_frame['avg_perf_metric'].max()
    data_frame['instr_mem_size'] = data_frame['instr_mem_size'].map(lambda x: (np.log2(x)))
    isize_max = data_frame['instr_mem_size'].max()
    #compute hv
    hv, nadir = chyv.compute_hv_nadir_as_list(new_df, mins, maxs)
    contribs = hv.contributions(nadir)
    contribs_df=pd.DataFrame(contribs, columns=['hypervolume'])
    #print(contribs_df.sort_values(by=['hypervolume'], ascending=False).head(5))
    # print(data_frame)
    #join
    labels_2 = data_frame_2.columns.values   
    labels = data_frame.columns.values 
    data_frame = data_frame.applymap(lambda x: abs(x))
    data_frame = data_frame.join(contribs_df)
    data_frame_joined = data_frame.join(data_frame_2)
    #idx_names= data_frame_joined[data_frame_joined['CLB LUTs*'] > 100].index
    #data_frame_joined.drop(idx_names, inplace=True)
    data_frame_joined = data_frame_joined.sort_values(by=['hypervolume'], ascending=False).head(5)
    data_frame_joined = data_frame_joined.sort_values(by=['frequency'])
    data_frame_joined = data_frame_joined.drop(columns='hypervolume')
    #TODO apply the filtering
    #filter
    #sort
    #drop



    #data_frame_joined = data_frame_joined.applymap(lambda x: abs(x))
    data_frame = data_frame_joined.drop(columns=labels_2)
    data_frame_2 = data_frame_joined.drop(columns=labels)

    #Take absolute values of data
    #Normalize frequency data (0-100) 
    fmax = data_frame['frequency'].max()
    data_frame['frequency'] = data_frame['frequency'].map(lambda x: (x / fmax))

    fig, ax = plt.subplots(2, 1, figsize=(16,10))
    ax[0].tick_params(axis='both', which='both', labelsize=ndovadomo_tick_lbls)
    ax[1].tick_params(axis='both', which='both', labelsize=ndovadomo_tick_lbls)

    ax2 = ax[0].twinx()
    ax2.tick_params(axis='both', which='both', labelsize=ndovadomo_tick_lbls)

    first_df=data_frame #.drop(columns=['instr_mem_size','avg_perf_metric'])
    labels = first_df.columns.values
    res_df = data_frame.drop(columns='frequency')

    maxres = max(res_df.max())
    res_df_only = res_df.apply(lambda x: x / maxres)

    width = 0.2
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

    tick_num=8
    ax2.set_yticks(np.linspace(0,1,num=tick_num))
    ax2.set_yticklabels(map(math.floor, np.linspace(0,fmax,num=tick_num)))
    ax[0].set_yticks(np.linspace(0,1,num=tick_num))
    ylabel_vals = np.linspace(0,maxres, num=tick_num)
    ylabel_vals = [round(x,2) for x in ylabel_vals]
    ax[0].set_yticklabels(ylabel_vals)
    if normalize_res:
        ax[0].set_ylabel('Scaled Metrics', fontsize=ndovadomo_fnt)
        # ax[0].set_ylabel('Resource Utilization (%)\nThroughput [Gb/s]\n2^x $I lines')
    else:
        ax[0].set_ylabel('Resources')
        ax[0].plot([0., len(x)], [100/maxres, 100/maxres], "k--")
        labels = np.append('100% Utilization',labels)
    ax[0].grid(visible=True, which='major', linestyle='dotted',axis='y',zorder=0)
    ax2.set_ylabel('Frequency (MHz)', fontsize=ndovadomo_fnt)

    ax[0].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.25), ncol=len(labels),fontsize=ndovadomo_leg_fonts)
    # ax[0].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=int(math.ceil(len(labels)/2)))


    labels = data_frame_2.columns.values
    width = 0.2
    x = np.arange(len(data_frame_2.index))
    offs = np.arange((-len(labels)/2)*width, (len(labels)/2)*width, width)
    i = 0
    for l in labels:
        ax[1].bar(x+offs[i], data_frame_2[l], width=width, color=colors[i],edgecolor='black',linewidth=0.5)
        i = i + 1
    ax[1].set_xticks(x)
        
    ax[1].margins(x=0.01)
    ax[1].set_yticks(np.arange(0,data_frame_2.max().max(),5))
    ax[1].set_ylabel('Design Parameters', fontsize=ndovadomo_fnt)
    ax[1].grid(visible=True, which='major', linestyle='dotted',axis='y')
    ax[1].set_xlabel('Solution', fontsize=ndovadomo_fnt)
    ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.25), ncol=len(data_frame_2.columns),fontsize=ndovadomo_leg_fonts)
    # ax[1].legend(shorten_labels(labels), loc='upper left', bbox_to_anchor=(0.0, 1.28), ncol=int(math.ceil(len(data_frame_2.columns)/2)))

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

