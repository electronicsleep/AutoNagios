#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 10/24/2017
# Purpose: AutoNagios: Generate Nagios host
# Released under the BSD license

# python3 generate_nagios_host.py -f "new_file2" -n "test" -i "127.0.0.1"

import argparse

parser = argparse.ArgumentParser(description='AutoNagios')

parser.add_argument("-f", "--filename", help="filename", required=True)
parser.add_argument("-n", "--hostname", help="host", required=True)
parser.add_argument("-i", "--ip", help="ip", required=True)

args = parser.parse_args()
print(args.filename)
print(args.hostname)
print(args.ip)


template_file = open("localhost_nagios2.tpl", "r")
create_file = ""

for line in template_file:
    new_line = ""
    if "localhost" in line:
        new_line = line.replace("localhost", args.hostname)
    elif "127.0.0.1" in line:
        new_line = line.replace("127.0.0.1", args.ip)
    else:
        new_line = line
    create_file += new_line

print("Created new Nagios file: " + args.filename + "_generated.cfg")
write_file = open(args.filename + "_generated.cfg", "w")
write_file.write(create_file)
