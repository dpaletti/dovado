TIREX_FOLDER=./results/tirex
CICERO_FOLDER=./results/cicero

python3 generate_graphs.py -d $TIREX_FOLDER/exact_many/ -n -cic -tir --hypervolume tirex
python3 generate_graphs.py -d $TIREX_FOLDER/approximate_many/ -r $TIREX_FOLDER/exact_many/ -n -cic -tir --hypervolume tirex
python3 generate_graphs.py -d $CICERO_FOLDER/exact/ -n -cic --hypervolume cicero
python3 generate_graphs.py -d $CICERO_FOLDER/approx/ -r $CICERO_FOLDER/exact/ -n -cic --hypervolume cicero

python3 generate_graphs.py -d results/corundum_exact -n
python3 generate_graphs.py -d results/corundum_approx -r results/corundum_exact -n 
python3 generate_graphs.py -d results/neorv32_exact
python3 generate_graphs.py -d results/neorv32_approx -r results/neorv32_exact 
