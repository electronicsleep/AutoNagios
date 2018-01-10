#!/bin/bash
HOSTS="m3cho.com forum.memoryecho.com yourideaspace.com"

EPOC=$(date "+%s")
DAY=$(date "+%d")
MONTH=$(date "+%m")
YEAR=$(date "+%Y")

for HOST in $HOSTS;
do
 IP=$(dig +short $HOST)
 echo "_______________________"
 echo "### HOST: $HOST IP: $IP"
 INFO=$(echo -ne '\n' | openssl s_client -showcerts -servername $HOST -connect $IP:443 | openssl x509 -inform pem -noout -enddate && echo -e '\r')
 echo "$INFO" > /tmp/ssl_info.txt
 EXPIRY=$(grep "notAfter" info.txt)
 EXPIRY_DATE=$(echo $EXPIRY | cut -f 2 -d =)
 EXPIRY_YEAR=$(echo $EXPIRY_DATE | cut -f 4 -d ' ')
 EXPIRY_DAY=$(echo $EXPIRY_DATE | cut -f 2 -d ' ')
 EXPIRY_MONTH=$(echo $EXPIRY_DATE | cut -f 1 -d ' ')

 OS=$(uname)
 if [ "$OS" == "Darwin" ]; then
  #MacOs
  echo "Found MacOS"
  COMPARE=$(date -j -f "%d %b %Y %T %Z" "$EXPIRY_DAY $EXPIRY_MONTH $EXPIRY_YEAR 00:00:00 PST" +"%s")
 else
  #Linux
  echo "Found Linux"
  COMPARE=$(date "+%s" -d "$EXPIRY_YEAR-$EXPIRY_DAY-$EXPIRY_MONTH 00:00:00 PST")
 fi
 
 SEC=$(expr $COMPARE - $EPOC)

 DAYS=$(expr $SEC / 86400)
 if [ "$DAYS" -lt 30 ]; then
  echo "Warning: Renew Cert $DAYS days left."
  exit 1
 elif [ "$DAYS" -lt 20 ]; then
  echo "Error: Renew Cert $DAYS days left."
  exit 2
 else
  echo "OK: you have time..."
 fi
done
