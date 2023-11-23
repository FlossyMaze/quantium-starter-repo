#!/bin/bash

# Activate the virtual environment
source ./venv/Scripts/activate

# Ensure that the virtual environment is activated
if [ -z "${VIRTUAL_ENV}" ]; then
    echo "Error: Virtual environment activation failed."
    exit 1
fi

# Install dependencies
pip install -r requirements.txt --upgrade

# Run the test suite using the Python executable within the virtual environment
./venv/Scripts/python -m pytest test_app.py

# Capture the exit code of the last command
PYTEST_EXIT_CODE=$?

# Return the exit code
if [ $PYTEST_EXIT_CODE -eq 0 ]; then
    exit 0  # All tests passed
else
    exit 1  # Something went wrong
fi
