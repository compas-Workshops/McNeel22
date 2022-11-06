#!/bin/sh

CONDA_ENV_NAME=mcneel22

if [ -z "$CONDA_EXE" ];then
    SYSTEM_ARCH=$(uname -p)
    if [ "$(uname -s)" = "Linux" ]; then
        SYSTEM_TYPE=Linux
    else
        SYSTEM_TYPE=MacOSX
    fi

    CONDA_HOME=$HOME/miniconda3_compas
    CONDA_EXE=$CONDA_HOME/bin/conda

    if [ ! -f "$CONDA_EXE" ]; then
        echo Installing miniconda...
        curl -S -s https://repo.anaconda.com/miniconda/Miniconda3-latest-$SYSTEM_TYPE-$SYSTEM_ARCH.sh -o ./miniconda-installer.sh
        bash ./miniconda-installer.sh -b -p $CONDA_HOME
        rm ./miniconda-installer.sh
        echo Installing miniconda... Done!
    fi

fi

echo Detecting virtual environment...
$CONDA_EXE run -n $CONDA_ENV_NAME python --version 2> /dev/null
if [ $? -ne 0 ]; then
    echo Creating virtual environment...
    $CONDA_EXE env create -n $CONDA_ENV_NAME -f https://dfab.link/mcneel22.yml
    echo Creating virtual environment... Done!
else
    echo Updating virtual environment...
    $CONDA_EXE env update -n $CONDA_ENV_NAME -f https://dfab.link/mcneel22.yml
    echo Updating virtual environment... Done!
fi

echo Installing COMPAS for Rhino...
$CONDA_EXE run -n $CONDA_ENV_NAME python -m compas_rhino.install
echo Installing COMPAS for Rhino... Done!
