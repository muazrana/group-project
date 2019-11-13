#! /bin/sh
while ! nc -z mysql 3306; do sleep 3; done
python create.py
python run.py
