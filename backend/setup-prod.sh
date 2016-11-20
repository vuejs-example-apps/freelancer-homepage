#!/bin/sh
echo 'This script will setup Freelance Homepage django project production environemnt for you\n'
# cp core/settings_local.prod.example core/settings_local.py

./setup-common.sh
. venv/bin/activate
pip install psycopg2 gunicorn

echo 'All done. you are ready to activate your virtual environment, create superuser and run the server'
echo "Use 'source venv/bin/activate', then './manage.py createsuperuser' and follow nginx/supervisorctl example instructions"
