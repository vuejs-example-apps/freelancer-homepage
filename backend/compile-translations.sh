#!/bin/sh
echo 'Compiling translations; you need to have gettext installed'
. venv/bin/activate
cd core
../manage.py compilemessages -l ru
cd ..
cd freelancer-homepage
../manage.py compilemessages -l ru
cd ..
echo '\n'
