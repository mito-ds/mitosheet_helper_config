#!/bin/bash -eu

echo "Setting up the mitosheet_helper_config development env"
echo "This might take a few moments..."

# Setup a new venv
rm -rf venv/
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -e ".[dev]"
