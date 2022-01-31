from common_charts import *
from locale import normalize
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.rcsetup as rcsetup
import numpy as np
import pandas as pd


movl_fnt = 20
legend_fnt = 16
movl_lwdth = 7

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
    ax.legend(fontsize=legend_fnt)
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
    ax.legend(fontsize=legend_fnt)    
    ax.grid(visible=True, which='major', linestyle='dotted')
    image_format = 'svg' # e.g .png, .svg, etc.
    image_name = name + '.svg'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    image_format = 'pdf' # e.g .png, .svg, etc.
    image_name = name + '.pdf'
    fig.savefig(image_name, format=image_format, bbox_inches = 'tight', dpi=1200)
    plt.close(fig)