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

verify everthing checks out for Nagios

/usr/sbin/nagios3 -v /etc/nagios3/nagios.cfg

service nagios3 restart

chgrp -R www-data nagiosgraph/

cd /usr/local/nagiosgraph

LOOKED UP
AH01630: client denied by server configuration

Found new config for apache 2.4


```
cat /etc/apache2/conf-enabled/nagiosgraph.conf

# enable nagiosgraph CGI scripts
ScriptAlias /nagiosgraph/cgi-bin "/usr/local/nagiosgraph/cgi"
<Directory "/usr/local/nagiosgraph/cgi">
   Options ExecCGI
   #AllowOverride None
   #Order allow,deny
   Require all granted
   Allow from all
#   AuthName "Nagios Access"
#   AuthType Basic
#   AuthUserFile NAGIOS_ETC_DIR/htpasswd.users
#   Require valid-user
</Directory>
# enable nagiosgraph CSS and JavaScript
Alias /nagiosgraph "/usr/local/nagiosgraph/share"
<Directory "/usr/local/nagiosgraph/share">
   #Options None
   #AllowOverride None
   #Order allow,deny
   Require all granted
   Allow from all
</Directory>
```

No data in rrd directory /usr/local/nagiosgraph/var/rrd

see if rrd being created

ls -l /usr/local/nagiosgraph/var/rrd

checking logging dir

/usr/local/nagiosgraph/var/log

/var/log/

chown -R nagios /usr/local/nagiosgraph/

chown -R nagios rrd

if graphs still dont work check the logs for anything related to insert.pl

service apache2 restart

my preference is to have tatical be the default

vim index.php

//$corewindow="main.php";
$corewindow="cgi-bin/tac.cgi";

#Now you should have a nice Nagios3 and NagiosGraph setup with allows you to graph anything including any custom scripts you need, any lanugage is supported.

#Nagios isnt the prettiest for graphs, good for researching trouble issues also setup graphite and graphana for custom dashboards.

##Next setup greylog and elk stack for logging
