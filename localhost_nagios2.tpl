# A simple configuration file for monitoring the local host
# This can serve as an example for configuring other servers;
# Custom services specific to this host are added here, but services
# defined in nagios2-common_services.cfg may also apply.
# 

define host{
        use                     generic-host
        host_name               localhost
        alias                   localhost
        address                 127.0.0.1
        }

# Define a service to check the disk space of the root partition
# on the local machine.  Warning if < 20% free, critical if
# < 10% free space on partition.

define service{
        use                             generic-service,nagiosgraph
        host_name                       localhost
        service_description             Disk Space Root
        check_command                   check_disk!20%!10%!/
        }



# Define a service to check the number of currently logged in
# users on the local machine.  Warning if > 20 users, critical
# if > 50 users.

define service{
        use                             generic-service,nagiosgraph
        host_name                       localhost
        service_description             Current Users
        check_command                   check_users!20!50
        }


# Define a service to check the number of currently running procs
# on the local machine.  Warning if > 250 processes, critical if
# > 400 processes.

define service{
        use                             generic-service,nagiosgraph
        host_name                       localhost
        service_description             Total Processes
		    check_command                   check_procs!250!400
        }



# Define a service to check the load on the local machine. 

define service{
        use                             generic-service,nagiosgraph
        host_name                       localhost
        service_description             Current Load
		    check_command                   check_load!5.0!4.0!3.0!10.0!6.0!4.0
        }
