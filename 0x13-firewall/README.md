## Firewall
> A firewall is a hardware or software security system. Two types of firesalls are network and host-based. The main function is to filter incoming and outgoing network traffic. ```telnet web-02.holberton.online 2222``` lets you check if port 2222 is open to web-02. Resources: [Wiki](https://en.wikipedia.org/wiki/Firewall_%28computing%29), [Digital Ocean Sample Code on ufw](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-14-04)

### Description of what each file shows:
Files that start with:
1. Script installs ufw firewall. Blocks incoming traffic except these TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP)

### Environment
* Language: Bash script
* OS: Ubuntu 14.04 LTS
* Web Server: installed firewall on web-01, web-02 running Nginx
* Load Balancer: installed firewall on lb-01 running HAProxy, SSL
* Style guidelines: [Shellscript for Bash](https://github.com/koalaman/shellcheck)

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

