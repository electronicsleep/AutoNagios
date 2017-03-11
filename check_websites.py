#!/usr/bin/env python
import requests

check_websites_list = []

with open('/usr/lib/nagios/plugins/check_websits_inventory.txt', 'rU') as f:
  for line in f:
     #print(line)
     check_websites_list.append(line)

#print("Website List:")
#print(check_websites_list)

for website in check_websites_list:
    website = website.strip()
    try:
        r = requests.get(website)
        print r
        print("OK: " + website)
    except:
        print( "ERROR: CHECK WEBSITE: " + website)
        exit(1)

print("ALL WEBSITES OK")
exit(0)
