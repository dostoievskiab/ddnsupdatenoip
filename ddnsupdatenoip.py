#! /usr/bin/python3
#Created 26-12-2017
#What is this? Python script to update dynamic ip address on NO-IP DDNS service
#WARNING!! This method is really insecure. You probably should use their DUC (Dynamic DNS Update Client).
# TODO: Set up some logging
import requests
from datetime import datetime
username = '' #NO-IP user name
password = '' #NO-IP password
domainname = '' #NO-IP domain name

reqIp = requests.get('https://api.ipify.org') #Request actual public dynamic ip address from ipify API
reqNoip = requests.get('https://'+ username + ':'+ password +'@dynupdate.no-ip.com/nic/update?hostname='+ domainname +'&myip=' + reqIp.text)
print(str(datetime.now()) + ' - ' + reqNoip.text)
