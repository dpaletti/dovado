import pygmo as pyg
import pandas as pd
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "d:n:m:M:", [])
except getopt.GetoptError:
    print("Use: generate_graphs.py -d <dovado out dir> -m <m1>:<m2>:<mN> -M <m1>:<m2>:<mN> -n N")
ref_dims = None
mins = None
maxs = None
for opt, arg in opts:
    if opt == "-n":
        ref_dims = arg
    if opt == "-d":
        input_dir_base = arg
    if opt == "-m":
        mins = arg
    if opt == "-M":
        maxs = arg

if ref_dims == None or mins == None or max == None:
    print("Use: generate_graphs.py -d <dovado out dir> -m <m1>:<m2>:<mN> -M <m1>:<m2>:<mN> -n N")
    exit(-1)
input_dir = input_dir_base + "/dovado_work"
objfr = pd.read_csv(input_dir + '/objective_space.csv')

max_list = maxs.split(":")
min_list = mins.split(":")
min_list = [float(x) for x in min_list]
max_list = [float(x) for x in max_list]

#Normalize data
labels = objfr.columns.values
i = 0
for l in labels:
    objfr[l] = (objfr[l]-min_list[i]) / (max_list[i]-min_list[i])
    i = i + 1
points = objfr.values.tolist()
H = len(objfr.columns.values)-1
r = 1 + 1/H
nadir = (H+1) * [r]

hv = pyg.hypervolume(points)
print("Reference point: ")
print(nadir)
print("Hypervolume metric: ")
print(hv.compute(nadir))
print("Contribution per solution: ")
print(hv.contributions(nadir))
