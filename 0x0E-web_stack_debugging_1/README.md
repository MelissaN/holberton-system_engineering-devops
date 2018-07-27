## Webstack Debugging #1

### Description of what each file shows:
0. Requirement: Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
can't curl
```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
```
after debugging, we should get
```
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```
1. Same as 0 except nginx does not need to be running
```
root@966c5664b21f:/# service nginx status
 * nginx is not running
```

### Environment
* Language: Bash script
* OS: Ubuntu 14.04 LTS
* Container: Docker
* Web Server: Apache
* Style guidelines: [Shellscript for Bash](https://github.com/koalaman/shellcheck)
* Resource: [Webstack debugging Intranet page](https://intranet.hbtn.io/concepts/68)
---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

