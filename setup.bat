@echo off

title library app

echo welcome to library app . this app developed by python and django framework from bashizade.dev

echo *********************** START APPLICATION ***********************

call .venv\Scripts\activate

echo *********************** VIRTUAL MACHINE STARTED ***********************

cd manage_library

echo *********************** DIRECTORY APP CHANGED ***********************

py manage.py makemigrations

py manage.py migrate

echo *********************** FILES MIGRATED ***********************

start http://127.0.0.1:8000

echo *********************** BROWSER OPENED ***********************

py manage.py runserver

echo *********************** SERVER RUNNIG ***********************

pause