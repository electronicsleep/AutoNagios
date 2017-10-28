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

# check that http services are running
define service {
        use                             generic-service,nagiosgraph
        host_name                       localhost 
        service_description             HTTP
        check_command                   check_http
}

# check that ssh services are running
define service {
        use                             generic-service,nagiosgraph
        host_name                       localhost
        service_description             SSH
        check_command                   check_ssh
}
