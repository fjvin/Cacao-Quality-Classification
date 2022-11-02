#!/bin/bash

# activate the virtual environment
source env/Scripts/activate

# clone labelImg package
LABELIMG_PATH="images/labelImagePackage"
if [ ! -d "$LABELIMG_PATH" ];
then
    mkdir $LABELIMG_PATH
	git clone https://github.com/tzutalin/labelImg $LABELIMG_PATH
fi

# setup labelImg package
cd $LABELIMG_PATH && pyrcc5 -o libs/resources.py resources.qrc

# run labelImg package
python labelImg.py