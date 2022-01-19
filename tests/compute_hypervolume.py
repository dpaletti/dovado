import pygmo as pyg
import pandas as pd
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "d:r:", [])
except getopt.GetoptError:
    print("Use: generate_graphs.py -d <dovado out dir> -r <r1>:<r2>:<rN>")

for opt, arg in opts:
    if opt == "-r":
        reference_dir_base = arg
    if opt == "-d":
        input_dir_base = arg


input_dir = input_dir_base + "/dovado_work"
objfr = pd.read_csv(input_dir + '/objective_space.csv')
#Take absolute values of data
#objfr = objfr.applymap(lambda x: abs(x))


labels = objfr.columns.values
points = objfr.values.tolist()
#nadir = [objfr[x].max()+abs(0.0*objfr[x].max()) for x in labels]
nadir = [100,100,100,-50]

mins = [objfr[x].min() for x in labels]

hv = pyg.hypervolume(points)
print(hv.compute(nadir))
print(hv.contributions(nadir))
print(nadir)
