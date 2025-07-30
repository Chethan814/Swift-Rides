#!/bin/bash
# build_files.sh
pip install -r requirements.txt
npm install
python manage.py tailwind build
python manage.py collectstatic --noinput --clear
python manage.py migrate 