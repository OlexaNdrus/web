#!/usr/bin/sh



sudo pip3 install django=2.0.0
sudo pip3 install --upgrade gunicorn

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/django.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
cd /home/box/web/
sudo gunicorn -c /home/box/web/etc/gunicorn.conf -b 0.0.0.0:8080 hello:app
sudo gunicorn -c /home/box/web/etc/django.conf -b 0.0.0.0:8000 ask.wsgi:application