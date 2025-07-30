#!/bin/bash
# build_files.sh

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install

# Build Tailwind CSS
python manage.py tailwind build

# Collect static files
python manage.py collectstatic --noinput --clear

# Run migrations
python manage.py migrate 