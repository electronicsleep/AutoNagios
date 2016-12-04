# AutoNagios

AutoNagios

## INSTALLING NAGIOSGRAPH ON NAGIOS3 AND APACHE2 DEBIAN

```
apt-get install nagios3

apt-get install rrdtool

apt-get install libnagios-object-perl

apt-get install librrds-perl

apt-get install libgd-gd2-perl

apt-get install libcgi-pm-perl
```

https://sourceforge.net/projects/nagiosgraph/files/nagiosgraph/

```
scp -r nagiosgraph-1.5.2.tar.gz thinkpad.local:/home/USER

tar xvfz nagiosgraph-1.5.2.tar.gz

cd nagiosgraph-1.5.2

perl install.pl
```

install necessary libraries

go with defaults on everything else

follow instructions at the end of install.pl

update nagios.cfg

update commands.cfg

once finished update services then a check load to nagiosgraph

verify everthing checks out for Nagios

```
/usr/sbin/nagios3 -v /etc/nagios3/nagios.cfg

service nagios3 restart
```


add services and updates to localhost to verify

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

```
/usr/sbin/nagios3 -v /etc/nagios3/nagios.cfg

service nagios3 restart
```

dir for nagiosgraph info

cd /usr/local/nagiosgraph

chgrp -R www-data /usr/local/nagiosgraph/

LOOKED UP ERROR IN LOG
AH01630: client denied by server configuration

Found new config "Require all granted" for apache 2.4


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

```
ls -l /usr/local/nagiosgraph/var/rrd
```

checking logging dir

update permissions and checking logs

/usr/local/nagiosgraph/var/log

/var/log/

```
chown -R nagios /usr/local/nagiosgraph/

chown -R nagios /usr/local/nagiosgraph/rrd
```

if graphs still dont work check the logs for anything related to insert.pl

```
service apache2 restart
```

my preference is to have tatical be the default

```
cd /usr/share/nagios3/htdocs
vim index.php
```

//$corewindow="main.php";

$corewindow="cgi-bin/tac.cgi";

### Now you should have a useful and free Nagios3 and NagiosGraph setup with allows you to graph anything including any custom scripts you need you just need to send it the exit code at the end of the script, any language is supported.

#More info on Nagios Plugins
https://www.nagios.org/downloads/nagios-plugins/

### Nagios isnt the best for dashboards of graphs for overall large systems, it is very good for researching small and server level issues though and automating healthchecks, security upgrades, builds, self healing scripts and operational tasks.

### You may want to also setup graphite and graphana or prometheus for custom dashboards or monitoring from a service level instead of server level issues to get a larger view of systems health and hit count.

## Next setup greylog and elk stack for more advanced logging.

## Hope this saves someone some time.

# Send me any questions or suggestions, Cheers!
