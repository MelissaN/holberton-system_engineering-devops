## Load balancer
> This project sets up all three servers with Nginx and installs a load balancer.
> Resources: [Software/Hardware Load Balancers](https://www.thegeekstuff.com/2016/01/load-balancer-intro/),
> [Load Balancer Algos](https://devcentral.f5.com/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms),
> [Intro to Load balance concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts),
> [HTTP header](https://www.techopedia.com/definition/27178/http-header),
> [Redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29),
> [Webstack Debugging Intranet Page](https://intranet.hbtn.io/concepts/68)

### Description of what each file shows:
Files that start with:
0. Script configures second web server so it's identical to first web server. Adds to HTTP header too.
1. Script installs HAproxy on load balancer server; uses roundrobin

### Environment
* Language: Bash scripts
* OS: Ubuntu 14.04 LTS
* Container: Docker
* Web Servers: Nginx; (338-lb-01: ssh ubuntu@104.196.27.36); (338-web-01: ssh ubuntu@35.229.54.225); (338-web-02: ssh ubuntu@35.231.225.251)
* Style guidelines: [Shellscript for Bash](https://github.com/koalaman/shellcheck)
---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

