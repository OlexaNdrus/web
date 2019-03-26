#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepik_web"
mysql -uroot -e "CREATE USER 'OlexaNdrus' IDENTIFIED BY '123';"
mysql -uroot -e "GRANT ALL ON stepik_web.* TO 'OlexaNdrus';"
mysql -uroot -e "FLUSH PRIVILEGES;"


python manage.py makemigrations qa
python manage.py migrate qa


