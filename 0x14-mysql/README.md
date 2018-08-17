## MySQL Master-Slave configuration
> SQL is installed on both Nginx web servers and configured so that the first
> is a Master and the second is a Slave.

### Resources:
* [Database defined](https://searchsqlserver.techtarget.com/definition/database)
* [Backup types](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [Backup strategy](https://www.databasejournal.com/features/mssql/developing-a-sql-server-backup-strategy.html)
* [DigitalOcean tutorial I followed exactly](https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql)

### Description of what each file shows:
* File 0 shows the sql config files for both webservers.
* File 1 shows a Bash script that creates a compressed archive of the database so that we're able to have backup in case of a flood, power outage, etc.

### Environment
* Language: Bash scripts
* OS: Ubuntu 14.04 LTS
* Web Servers: (2) Nginx [35.229.54.225] [35.231.225.251], (1) HAproxy load balancer [104.196.27.36]
* Style guidelines: [Shellscript for Bash](https://github.com/koalaman/shellcheck)

---
### Authors
Melissa Ng [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/MelissaNg__)
