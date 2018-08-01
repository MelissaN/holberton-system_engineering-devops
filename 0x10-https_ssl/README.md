## HTTPS SSL
> HTTPS is a secure version of HTTP, used to encrypt all communication between
> the client and the website servers. When setting up HTTPS on our website,
> we should place the certificate on our website web server(s). Resources:
> [SSL](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html),
> [Step-by-Step Guide I followed to create SSL certificate!](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04),
> [HTTP to HTTPS](https://www.instantssl.com/ssl-certificate-products/https.html),
> [sample Bash functions taking parameters](http://tldp.org/LDP/abs/html/complexfunct.html)

### Description of what each file shows:
Files that start with:
1. running the script shows our subdomain and A records
2. shows HAproxy config file after creating SSL certificate. HAproxy is listening to port TCP 443 and accepts SSL traffic.
3. shows HAproxy config file again. Redirects HTTP traffic to HTTPS. HAproxy returns a 301 permanent redirect.

### Environment
* Language: Bash script
* OS: Ubuntu 14.04 LTS
* Web Server: Nginx
* Domain Name: from [Gandi](https://www.gandi.net/en)
* Style guidelines: [Shellscript for Bash](https://github.com/koalaman/shellcheck)

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)

