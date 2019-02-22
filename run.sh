#!/bin/bash

ARGS_LIST=$1

echo "Installing necessary packages"
pip3 install nltk
echo "Done installing"

echo "Run project file"
python3 analyzing_step/manager.py
echo "The graph saved in the 'Graphs' folder with the app name."



