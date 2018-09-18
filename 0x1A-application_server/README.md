## Application Server for Airbnb
> Task is to add application server to infrastructure, plug into Nginx, and serve Airbnb Clone projecct.

### Resources:
* [Application Server vs. Web Server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [Digital Ocean tutorial I followed - Serve Flask Applications with Gunicorn and Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04)
* [Gunicorn documentation](http://docs.gunicorn.org/en/latest/run.html)
* [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

### How it's done:
* Script 0-welcome_gunicorn-upstart_config shows newly created /etc/init/airbnb-onepage.conf file that starts Gunicorn instance to serve web_flask/0-hello_route.py from AirBnB_clone_v2
* Script 0-welcome_gunicorn-nginx_config shows modified /etc/nginx/sites-available/default file that now points 127.0.0.1:8000/airbnb-one-page/ to Gunicorn instance
```
ubuntu@web01$ sudo service airbnb-onepage start
 airbnb-onepage start/running, process 17981
ubuntu@web01$ curl http://127.0.0.1:8000
 Hello HBNB!
ubuntu@web01$ curl http://127.0.0.1/airbnb-onepage/
Hello HBNB!
```
* Script 1-pass_parameter-upstart_config shows newly created /etc/init/airbnb-onepage.conf file that starts Gunicorn instance to serve web_flask/6-number_odd_or_even.py from AirBnB_clone_v2
* Script 1-pass_parameter-nginx_config shows modified /etc/nginx/sites-available/default file that now points 127.0.0.1:8000/airbnb-dynamic/ to Gunicorn instance
```
ubuntu@web01$ sudo service airbnb-parameter start
 airbnb-parameter start/running, process 18155
ubuntu@web01$ curl 127.0.0.1:8001/number_odd_or_even/1
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 1 is odd</H1>
    </BODY>
</HTML>
ubuntu@web01$ curl http://127.0.0.1/airbnb-dynamic/number_odd_or_even/1
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 1 is odd</H1>
    </BODY>
</HTML>
```
* 

### Environment
* Technologies: Gunicorn, Upstart scripts
* OS: Ubuntu 14.04 LTS
* Web Server: Nginx

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)
