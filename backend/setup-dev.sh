#!/bin/sh
echo 'This script will setup Freelance Homepage django project development environemnt for you\n'
# cp core/settings_local.dev.example core/settings_local.py

./setup-common.sh
. venv/bin/activate

# echo 'Generating Fake Data'
# ./manage.py populate_fake
# echo '\n'

echo 'All done. you are ready to activate your virtual environment, create superuser and run the development server'
echo "Use 'source venv/bin/activate', then './manage.py createsuperuser' and './manage.py runserver_plus'"
