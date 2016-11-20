#!/bin/sh
echo 'Making translations; you need to have gettext installed'
. venv/bin/activate
cd core
../manage.py makemessages -l ru
cd ..
cd freelancer-homepage
../manage.py makemessages -l ru
cd ..
echo '\n'
