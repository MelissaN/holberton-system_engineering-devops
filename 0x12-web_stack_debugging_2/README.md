## Web stack debugging #2
> "Although NGINX master process is typically started with root privileges in order to listen on port 80 and 443, it can and should run as another non-root user in order to perform the web services... One of the best ways to reduce your exposure to attack when running a web server is to create a unique, unprivileged user and group for the server application." -[Run NGINX Web Server as non-root user](https://github.com/GSA/ansible-https-proxy/issues/1) The root user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.

### Description of what each file shows:
Files that start with:
0. script runs as another user
1. script configures nginx to be running as nginx user and not root; listens on all active IPs on port 8080. After debugging we should see:
```
root@ab6f4542747e:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@ab6f4542747e:~#
root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
0
root@ab6f4542747e:~#
```

### Environment
* Language: Bash scripts
* OS: Ubuntu 14.04 LTS
* Web Server: Nginx
* Style guidelines: [Shellscript for Bash](https://github.com/koalaman/shellcheck)

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

