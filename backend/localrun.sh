#! /bin/sh
if [ -d ".venv" ];
then 
    echo "Enabling virtual environment"
    source .venv/Scripts/activate
    export FLASK_ENV=development
    python main.py

else
    echo "No virtual environment was found"
    exit N
fi

