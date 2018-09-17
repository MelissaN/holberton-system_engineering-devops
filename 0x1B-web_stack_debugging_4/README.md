## Webstack Debugging #4
> We are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests. For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed.
```
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   0.353 seconds
Complete requests:      2000
Failed requests:        943 <--------------------------------------- =(
   (Connect: 0, Receive: 0, Length: 943, Exceptions: 0)
Non-2xx responses:      1057
Total transferred:      1196526 bytes
HTML transferred:       789573 bytes
Requests per second:    5664.01 [#/sec] (mean)
Time per request:       17.655 [ms] (mean)
Time per request:       0.177 [ms] (mean, across all concurrent requests)
Transfer rate:          3309.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       8
Processing:     2   17   3.8     17      24
Waiting:        2   17   3.8     17      24
Total:          9   17   3.3     17      24

Percentage of the requests served within a certain time (ms)
  50%     17
  66%     19
  75%     20
  80%     20
  90%     21
  95%     23
  98%     23
  99%     23
 100%     24 (longest request)
```

### Resources:
* [Max open files](https://stackoverflow.com/questions/27849331/how-to-set-nginx-max-open-files)

### How to debug:
* Run ApacheBench to simulate requests to server ```ab -c 100 -n 2000 localhost/```
* Look on /var/log/nginx/error.log. for errors and find "accept4() failed (24: Too many open files)"
* Google error message and try different solutions pertaining to resetting max files open limit [1](https://www.cyberciti.biz/faq/linux-unix-nginx-too-many-open-files/) [2](https://gist.github.com/joewiz/4c39c9d061cf608cb62b)
* Ultimate solution that solved the issue is modifying limit in ```/etc/default/nginx``` file
* Execute puppet script to automate solving issue across magnitude of servers ```puppet apply [0-filename]```

### Environment
* Language: Puppet config script
* OS: Ubuntu 14.04 LTS
* Web Server: Nginx on Docker container
* Style guidelines: Puppet-lint
---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)
