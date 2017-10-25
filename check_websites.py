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
    print("ERROR: NO WEBSITES DEFINED")
    exit(1)

for website in check_websites_list:
    website = website.strip()
    try:
        r = requests.get(website)
        print(r)
        print("OK: " + website)
    except Exception as e:
        print("ERROR: CHECK WEBSITE: " + website + " " + str(e) + " | error=1 ")
        exit(1)

print("ALL WEBSITES OK | error=0")
exit(0)
