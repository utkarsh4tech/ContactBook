#! /bin/sh
if [ -d ".venv" ];
then
    echo ".venv folder found, installing dependencies using pip3"
else 
    echo ".venv folder is not found, creating a virtual environment"
    python3 -m venv .venv
fi

source .venv/Scripts/activate
pip3 install -r requirements.txt
