sudo apt remove python-django -y
sudo apt remove gunicorn -y

sudo apt update
sudo apt install python3-pip

pip3 install django==2.0.0
pip3 install gunicorn