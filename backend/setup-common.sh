#!/bin/sh
echo 'Creating python3 virtual environment'
virtualenv -p python3 venv
echo '\n'

echo 'Activating virtual environment'
. venv/bin/activate
echo '\n'

echo 'Installing dependencies'
pip install -r requirements.txt
echo '\n'

echo 'Compiling translations; you need to have gettext installed'
./compile-translations.sh

echo 'Initializing database structure'
./manage.py migrate
echo '\n'

# echo 'Installing fixtures'
# echo ' - somemodel'
# ./manage.py loaddata somemodel/fixtures/somefixture.json
# echo '\n'
