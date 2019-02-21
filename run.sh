#!/bin/bash

ARGS_LIST=$1

echo "Installing necessary packages"
pip install nltk
echo "Done installing"

echo "Run project file"
python analyzing_step/manager.py
echo "The graph saved in the 'Graphs' folder with the app name."
sleep 50


