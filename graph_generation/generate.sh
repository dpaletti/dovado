python3 generate_graphs.py -d results/tirex_nags31/exact_many_restricted_alone/ -n -cic -tir --hypervolume tirex
python3 generate_graphs.py -d results/tirex_nags31/approximate_many_restricted_alone/ -r results/tirex_nags31/exact_many_restricted_alone/ -n -cic -tir --hypervolume tirex
python3 generate_graphs.py -d results/cicero_cf_nags21/exact_cf_rawperf/ -n -cic --hypervolume cicero
python3 generate_graphs.py -d results/cicero_cf_nags25/approx_cf_rawperf/ -r results/cicero_cf_nags21/exact_cf_rawperf/ -n -cic --hypervolume cicero

