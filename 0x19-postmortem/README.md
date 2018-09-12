<p align="center">
<img src="https://raw.githubusercontent.com/MelissaN/holberton-system_engineering-devops/master/0x19-postmortem/youtube500error.jpg" width=75% height=75%/>
</p>

## Service unavailability
### Incident report for [Site Outage](https://raw.githubusercontent.com/MelissaN/holberton-system_engineering-devops/master/0x19-postmortem/youtube500error.jpg)

#### Issue Summary
On September 11th, 2018 from 9:39 AM to 9:49 AM UTC, the company's website was down for ten minutes. 100% of users experienced a 500 internal server error caused by a mispelled filename in a configuration file.

#### Timeline
* 9:39 AM   Sitewide update deployed; outage begins
* 9:40 AM   Error logs checked by DevOps team
* 9:43 AM   Configuration updated to log extra errors
* 9:45 AM   Filename error caught in config file
* 9:47 AM   Execute Puppet manifest across all company servers
* 9:49 AM   100% restored and back online

#### Root Cause and Resolution
After a small sitewide update was deployed without first being tested, outage to the site began. When no errors were found in our 'error.log' files we modified our configuration file to allow for more erorr logging. With the help of 'strace,' it appeared an accidental filename mispelling triggered errors when the site was requested. The server was attempting to locate the file as normal procedure but failed to find the file ending in ".phpp" when it should be looking for ".php" After changing this line in the '/var/www/html/wp-settings.php' file, tests suceeded to show the site. A puppet manifest was written and executed across all company servers immediately after to restore service.

#### Corrective and Preventative Measures
After a discussion it has been decided we can prevent this in the future by:
* Modifying configuration files for more error logging to quicken response times
* Test before deploying on all servers no matter how small an update
This is only a small incident so we are doing great! Thanks for your patience and your continued confidence in us.
