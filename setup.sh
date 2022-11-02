#!/bin/bash

# create virtual environment
python -m venv env

# activate the virtual environment
source env/Scripts/activate

# upgrade pip
python -m pip install --upgrade pip

# install project dependencies
python -m pip install -r requirements.txt

# create images folder
mkdir images
mkdir images/collectedImages
mkdir images/labelImagePackage