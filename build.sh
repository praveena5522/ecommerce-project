#!/bin/bash
# build.sh — Django build automation script

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate
