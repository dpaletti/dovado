import matplotlib
import matplotlib.pyplot as plt
import matplotlib.rcsetup as rcsetup
import numpy as np
import pandas as pd

colors = ['#c7e9b4', '#7fcdbb', '#41b6c4', '#1d91c0', '#225ea8']

def split_binary_df(data_frame):
    labels = data_frame.columns.values
    c = data_frame.columns[data_frame.isin([0,1]).all()]
    bindf = data_frame[c].copy()
    data_frame.drop(columns=c, axis=1, inplace=True)
    return bindf


def shorten_labels(labels):
    shorthand = {'Slice LUTs*' : 'LUTs', 'Slice Registers' : 'FF', 'Block RAM Tile':'BRAM', 'frequency' : 'Freq.', \
    'NCluster': 'NClstr', 'ClusterWidth':'ClstrWdt', 'CLB LUTs*' : 'LUTs [%]', 'CLB Registers' : 'FF [%]',\
    'instr_mem_size':'$I_AddrSz  [2^x lines]', 'avg_perf_metric':'AVG_Gbps', 'AddressWidthInstr':'$I_AddrSz', \
    'AddressWidthData':'$D_AddrSz', 'BB_N':'#Engn','CC_ID_BITS':'Window','PC_WIDTH':'$I_AddrSz', \
    'avg_gbps_per_luts': 'Gbps/LUTs', 'QUEUE_INDEX_WIDTH':'QUE_IDX_WDT', 'OP_TABLE_SIZE':'OP_TAB_SZ' }
    nlbl = []
    for l in labels:
        if l in shorthand:
            nlbl.append(shorthand[l])
        else:
            nlbl.append(l)
    return nlbl


tirex_mins=[-512.0, 0.0, 0.0, -60.0, -500.0]
tirex_maxs=[-8.0, 150.0, 150.0, -1.0, -100.0]
cicero_mins=[0.0, -1024.0, -20.0, -200.0]
cicero_maxs=[100.0, -512.0, -1.0, -50.0]
neorv_mins=[0.0, 0.0, -8000.0, 0.0]
nerov_maxs=[100.0, 100.0, 0.0, 100.0]
corundum_mins=[0.0, 0.0, 0.0, -300.0]
corundum_maxs=[100.0, 100.0, 100.0, 0.0]