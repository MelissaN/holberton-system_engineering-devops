# created new file /etc/init/airbnb-onepage.conf in web server 1
description "Gunicorn application server running 0-hello_route flask app"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid ubuntu
setgid root

chdir /home/ubuntu/AirBnB_clone_v2/web_flask
exec gunicorn --workers 1 --bind 127.0.0.1:8000 -m 007 0-hello_route:app