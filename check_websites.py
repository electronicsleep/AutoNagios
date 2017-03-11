#!/usr/bin/env python
import requests
import os

cwd = os.getcwd()

#Running Via Nagios
if cwd == '/':
  cwd = '/usr/lib/nagios/plugins/'

path = os.path.join(cwd, "check_websites_inventory.txt")

check_websites_list = []

with open(path, 'rU') as f:
  for line in f:
     #print(line)
     check_websites_list.append(line)

#print("Website List:")
#print(check_websites_list)

if len(check_websites_list) == 0:
    print("ERROR: NO WEBSITES DEFINED")
    exit(1)


for website in check_websites_list:
    website = website.strip()
    try:
        r = requests.get(website)
        print r
        print("OK: " + website)
    except:
        print("ERROR: CHECK WEBSITE: " + website + " | 1")
        exit(1)

print("ALL WEBSITES OK | 0")
exit(0)
