#!/bin/bash

# NOTE: This script is used to initialize the environment for the project.
module load python/3.14

if [ ! -d "venv_prepro" ]; then
    python3 -m venv venv_prepro
fi


source venv_prepro/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
echo "Environment initialized successfully for Rank: $PROC_RANK"






