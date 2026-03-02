#!/bin/bash
export N_PROCS=20000

source venv_prepro/bin/activate

# Launch the 20,000 workers
super_duper_process_spawner -n $N_PROCS python text_preprocessor.py

echo "Finished preprocessing data."