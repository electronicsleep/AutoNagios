#!/bin/bash
MSG=$1
URL=""
USER="@user"
if [ -z "$URL" ];then
 echo "Error: No url set"
 exit 1
fi
curl -X POST --data-urlencode "payload={\"channel\": \"#alerts\", \"username\": \"webhookbot\", \"text\": \"$MSG bot $USER.\", \"icon_emoji\": \":ghost:\"}" $URL
echo ": slack message sent"
