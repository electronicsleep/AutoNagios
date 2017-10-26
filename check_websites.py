#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 07/03/2017
# Purpose: AutoNagios: Example Python check
# Released under the BSD license

import requests
import os

cwd = os.getcwd()

if cwd == '/':
    cwd = '/usr/lib/nagios/plugins/'

path = os.path.join(cwd, "check_websites_inventory.txt")

check_websites_list = []

with open(path, 'rU') as f:
    for line in f:
        check_websites_list.append(line)

if len(check_websites_list) == 0:
    print("Error: No websites defined")
    exit(1)

for website in check_websites_list:
    website = website.strip()
    try:
        r = requests.get(website)
        print(r)
        print("OK: " + website)
    except Exception as e:
        print("Error: Check website: " + website + " " + str(e) + " | error=1")
        exit(1)

print("All websites ok | error=0")
exit(0)
