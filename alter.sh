virtualenv -p python3 myvenv
source myvenv/bin/activate
pip install --upgrade pip
pip install django
pip install gunicorn

cd /home/box/ask
gunicorn --bind=0.0.0.0:8000 --workers=2 --timeout=15 --log-level=debug ask.wsgi:application