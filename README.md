# AutoNagios

- Notes on how to install graphing plugin NagiosGraph with Nagios.

- How to install a example custom check.

## Installing NagiosGraph on Nagios3 and Apache2 on Debian8

```
# Base packages
apt-get install fail2ban vim git tree -y

# Nagios core
apt-get install nagios3 nagios-plugins rrdtool -y

# Install necessary libraries for NagiosGraph
apt-get install libnagios-object-perl librrds-perl libgd-gd2-perl libcgi-pm-perl -y

```

## NagiosGraph
https://sourceforge.net/projects/nagiosgraph/files/nagiosgraph/

```
tar xvfz nagiosgraph-*.tar.gz

cd nagiosgraph-*

perl install.pl --check-prereq

perl install.pl
```

go with defaults on everything else

say yes to modify configs

apache config location /etc/apache2/conf-enabled/

## Verify config

```
/usr/sbin/nagios3 -v /etc/nagios3/nagios.cfg

/etc/init.d/nagios3 restart

/etc/init.d/apache2 restart
```

## For manual config /check

check/follow instructions at the end of install.pl

update nagios.cfg

update commands.cfg

once finished update services then a check load to nagiosgraph

verify everthing checks out for Nagios

add services and updates to localhost to verify

## Update services

```
vim /etc/nagios3/conf.d/services_nagios2.cfg

define service {
        name nagiosgraph
        action_url /nagiosgraph/cgi-bin/show.cgi?host=$HOSTNAME$&service=$SERVICEDESC$
        register 0
}
```

Update use statement and add nagiosgraph

```
sed -i 's/generic-service/generic-service,nagiosgraph/g' /etc/nagios3/conf.d/localhost_nagios2.cfg
sed -i 's/generic-service/generic-service,nagiosgraph/g' /etc/nagios3/conf.d/services_nagios2.cfg

#Example
define service{
        use                             generic-service,nagiosgraph
        host_name                       localhost
        service_description             Current Load
```

Now you should have graph icon on each service check

Update apache permissions to allow

Verify everthing checks out for Nagios

```
/usr/sbin/nagios3 -v /etc/nagios3/nagios.cfg

service nagios3 restart
```

## Dir for nagiosgraph info

cd /usr/local/nagiosgraph

Edit Apache config to allow Nagios access to graphs

vim /etc/apache2/conf-enabled/nagiosgraph.conf

```
# enable nagiosgraph CGI scripts
ScriptAlias /nagiosgraph/cgi-bin "/usr/local/nagiosgraph/cgi"
<Directory "/usr/local/nagiosgraph/cgi">
   Options ExecCGI
   Require all denied
   AuthName "Nagios Access"
   AuthType Basic
   AuthUserFile /etc/nagios3/htpasswd.users
   Require valid-user
</Directory>
# enable nagiosgraph CSS and JavaScript
Alias /nagiosgraph "/usr/local/nagiosgraph/share"
<Directory "/usr/local/nagiosgraph/share">
   Options None
   Require all denied
   AuthName "Nagios Access"
   AuthType Basic
   AuthUserFile /etc/nagios3/htpasswd.users
   Require valid-user
</Directory>
```

Check data in rrd directory 

tree /usr/local/nagiosgraph/var/rrd

## Troubleshooting

Checking logs

tail -f /usr/local/nagiosgraph/var/log/nagiosgraph.log

tail -f /var/log/apache2/error.log /var/log/nagios3/nagios.log

If graphs dont work check the logs for anything related to insert.pl

My preference is to have tactical be the default

```
vim /usr/share/nagios3/htdocs/index.php
//$corewindow="main.php";
$corewindow="cgi-bin/tac.cgi";
```

Now you should have a useful and free Nagios3 and NagiosGraph setup with allows you to customize and  graph anything including any custom scripts you need you just need to send the exit code and proper perfdata. I also suggest using version control and deployment process on your configs. 

## More info on Nagios Plugins
https://www.nagios.org/downloads/nagios-plugins/

## Enable external checks 
- So you can re-schedule checks via the web interface
```
vim /etc/nagios3/nagios.cfg
check_external_commands=1

service nagios3 stop
dpkg-statoverride --update --add nagios www-data 2710 /var/lib/nagios3/rw
dpkg-statoverride --update --add nagios nagios 751 /var/lib/nagios3
service nagios3 start
```

## Setup Simple Python Check
```
# setup pip and requests on Nagios machine

apt-get install python-pip
pip install requests

vim /etc/nagios3/conf.d/localhost_nagios2.cfg

# A list of external websites to check

define service{
        use                             generic-service,nagiosgraph
        host_name                       localhost
        service_description             Current Websites
        check_command                   check_websites
        }

# Plugin DIR

cd /etc/nagios-plugins/config
vim check-websites.cfg

# 'check_websites' command definition
define command{
        command_name    check_websites
        command_line    /usr/lib/nagios/plugins/check_websites.py
        }

cp check_websites.py /usr/lib/nagios/plugins/
cp check_websites_inventory.txt /usr/lib/nagios/plugins/

chmod 755 /usr/lib/nagios/plugins/check_websites.py

# verify it works
vim /usr/lib/nagios/plugins/check_websites_inventory.txt
python /usr/lib/nagios/plugins/check_websites.py

# restart Nagios
/usr/sbin/nagios3 -v /etc/nagios3/nagios.cfg
service nagios3 restart
```

## Changing Nagios3 password

```
mv /etc/nagios3/htpasswd.users /etc/nagios3/htpasswd.users.backup
htpasswd -c /etc/nagios3/htpasswd.users nagiosadmin
```


#### For Dashboards of combined or overlayed graphs you may want to also setup Grafana, Prometheus or Graphite for custom dashboards or monitoring from a dashoard level instead of server level to get a larger view of systems health and hit count.

Hope this saves someone some time.

## Send me any questions or suggestions, Cheers!
