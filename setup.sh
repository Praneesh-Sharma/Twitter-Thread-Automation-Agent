#!/bin/bash

echo "Setting up the Multi-Agent System Project..."

# Create virtual environment
python3 -m venv venv
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Copy config template
if [ ! -f config/config.json ]; then
  cp config/config_template.json config/config.json
  echo "config.json created. Please fill in your API keys in config/config.json."
else
  echo "config.json already exists."
fi

echo "Setup complete! Activate your virtual environment with 'source venv/bin/activate'."
