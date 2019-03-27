#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web CHARACTER SET utf8;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'OlexaNdrus'@'localhost' WITH GRANT OPTION;"


#python manage.py makemigrations qa
#python manage.py migrate qa

