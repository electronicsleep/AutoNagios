#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 07/03/2017
# Purpose: AutoNagios: Example Python check
# Released under the BSD license

import requests
import os

nagios_dir = "/usr/lib/nagios/plugins/"
if os.path.exists(nagios_dir):
    cwd = nagios_dir
    print("Using nagios dir")
else:
    print("Using local dir")
    cwd = '.'

path = os.path.join(cwd, "check_websites_inventory.txt")

check_websites_list = []

with open(path, 'rU') as f:
    for line in f:
        check_websites_list.append(line)

if len(check_websites_list) == 0:
    print("Error: No websites defined")
    exit(1)

count = 0
for website in check_websites_list:
    website = website.strip()
    count += 1
    try:
        r = requests.get(website)
        # print(r)
        # print("OK: " + website)
    except Exception as e:
        print("Error: Check website: " + website + " " + str(e) + " | error=1")
        exit(1)

print("All websites ok " + str(count) + " | error=0")
exit(0)
