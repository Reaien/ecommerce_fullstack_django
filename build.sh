#!/bin/bash
chmod +x build.sh
pip install -r requirements.txt
python manage.py collectstatic --noinput