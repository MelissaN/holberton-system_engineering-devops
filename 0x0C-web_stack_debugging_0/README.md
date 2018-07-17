## Web stack debugging #0

### Description of what each file shows:
0. After installing Apache, we get an error message (curl: (56) Recv failure: Connection reset by peer OR curl: (52) Empty reply from server) when running ```curl 0:8080```. We fix it by starting Apache service.
```
vagrant@vagrant-ubuntu-trusty-64$ sudo apt install apache2
vagrant@vagrant-ubuntu-trusty-64$ docker run -p 8080:80 -d -it holbertonschool/265-0d275ce8cffc10fa1fab33f6d61d40b6530e3693c7bf097128be6d51ac63c0fda
vagrant@vagrant-ubuntu-trusty-64$ curl 0:8080
curl: (56) Recv failure: Connection reset by peer -OR- curl: (52) Empty reply from server
vagrant@vagrant-ubuntu-trusty-64$ sudo service apache2 start #fix it
```

### Environment
* Language: Bash script
* OS: Ubuntu 14.04 LTS
* Container: Docker
* Web Server: Apache
* Style guidelines: [Shellscript](https://github.com/koalaman/shellcheck)
---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

