## Webstack Debugging #3
> Learning to debug Apache and WordPress with ```strace``` and ```error.log``` files.

```
# In one terminal of given buggy Docker container
$ cat /var/log/apache2/error.log # no error found; weird

# Set 'display_errors' to 'On' in /etc/php5/apache2/php.ini [resource](https://stackoverflow.com/questions/4731364/internal-error-500-apache-but-nothing-in-the-logs)
$ sudo service apache2 restart

# 'curl -sI 127.0.0.1' now returns status 200 but 'curl -s 127.0.0.1:80 | grep Holberton' doesn't return expected output
$ ps -auxf
$ strace -p <pid of apache2>

# Strace will wait so curl in another terminal to watch for error message
# After curling in other terminal, we see 'open("/var/www/html/wp-includes/class-wp-locale.php
", O_RDONLY) = -1 ENOENT (No such file or directory)'
# Opening /var/log/apache2/error.log, we see 'PHP Fatal error: require_once(): Failed opening required '/var/www/html/wp-includes/class-wp-locale.phpp' (include_path='.:/usr/share/php:/usr/share/pear') in /var/www/html/wp-settings.php on line 137'
$ emacs /var/www/html/wp-settings.php # line 137 fix spelling error from '.phpp' to '.php'
```

```
# In another terminal
$ curl -sI 127.0.0.1
$ curl -s 127.0.0.1:80 | grep Holberton
```

### Resources:
* [Look at apache2 error log](https://stackoverflow.com/questions/4731364/internal-error-500-apache-but-nothing-in-the-logs)

### Description of what each file shows:
0- Usage: ```puppet apply 0-strace_is_your_friend.pp``` to automate fixing this particular error

### Environment
* OS: Ubuntu 14.04 LTS
* Container: Docker
* Web Server: Apache with WordPress
* Automation Script to solve issue: Puppet
---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)
