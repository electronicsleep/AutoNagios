#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 10/24/2017
# Purpose: AutoNagios: Generate Nagios hosts from inventory file
# Released under the BSD license

# python3 generate_nagios_inventory.py

inventory_file = open("inventory.txt", "r")

for line in inventory_file:
    if line.startswith("#"):
        print("Comment:" + line)
        continue
    hostname = line.split(" ")[0]
    ip = line.split(" ")[1]
    print("Host: " + hostname)
    print("IP: " + ip)

    template_file = open("localhost_nagios2.tpl", "r")
    create_file = ""

    for line2 in template_file:
        new_line = ""
        if "localhost" in line:
            new_line = line2.replace("localhost", hostname)
        elif "127.0.0.1" in line:
            new_line = line2.replace("127.0.0.1", ip)
        else:
            new_line = line2
        create_file += new_line

    print("Created new Nagios file: " + hostname + "_generated.cfg")
    write_file = open(hostname + "_generated.cfg", "w")
    write_file.write(create_file)
