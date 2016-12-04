# AutoNagios

AutoNagios

## INSTALLING NAGIOSGRAPH ON NAGIOS3 AND APACHE2 DEBIAN

apt-get install nagios3

apt-get install rrdtool

apt-get install libnagios-object-perl

apt-get install librrds-perl

apt-get install libgd-gd2-perl

apt-get install libcgi-pm-perl

https://sourceforge.net/projects/nagiosgraph/files/nagiosgraph/

scp -r nagiosgraph-1.5.2.tar.gz thinkpad.local:/home/chris

tar xvfz nagiosgraph-1.5.2.tar.gz

perl install.pl

install necessary libraries

go with defaults

follow instructions

update nagios.cfg

update commands.cfg

once finished update services then a check load


```
vim /etc/nagios3/conf.d/services_nagios2.cfg

define service {
name nagiosgraph
action_url /nagiosgraph/cgi-bin/show.cgi?host=$HOSTNAME$&service=$SERVICEDESC$
register 0
}
```

Update like so 

vim /etc/nagios3/conf.d/localhost_nagios2.cfg

```
define service{
        use                             generic-service,nagiosgraph       ; Name of service template to use
        host_name                       localhost
        service_description             Current Load
```

update apache permissions to allow

/usr/sbin/nagios3 -v /etc/nagios3/nagios.cfg

chgrp -R www-data nagiosgraph/

cd /usr/local/nagiosgraph

LOOKED UP
AH01630: client denied by server configuration

Found new config for apache 2.4


No data in rrd directory /usr/local/nagiosgraph/var/rrd

see if rrd being created
ls -l /usr/local/nagiosgraph/var/rrd

chown -R nagios /usr/local/nagiosgraph/

chown -R nagios rrd

if graphs still dont work check the logs for anything related to insert.pl

my preference is to have tatical be the default

vim index.php

//$corewindow="main.php";
$corewindow="cgi-bin/tac.cgi";

#Now you should have a nice Nagios3 and NagiosGraph setup with allows you to graph anything including any custom scripts you need.
