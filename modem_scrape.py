#!/usr/bin/python3.6

import sys
from requests.auth import HTTPBasicAuth
from requests_html import HTMLSession
import time


session = HTMLSession()
session.auth = ('admin', 'password')

response = session.get('http://192.168.100.1/DocsisStatus.htm')
response2 = session.get('http://192.168.100.1/DocsisStatus.htm')
response2.html.render(retries=1,scrolldown=0,wait=1,reload=False)

startup = response2.html.search(' var tagValueList = \'{}\';\n\n    return')[0]
up = response2.html.search('|4|Not Locked|Unknown|0|0|0|0.0";\n*/\n    var tagValueList = \'{}\';\n\n    return')[0]
down = response2.html.search('|8|Not Locked|Unknown|0|0|0.0|0.0|0|0";\n*/\n    var tagValueList = \'{}\';\n\n    return')[0]

now = time.strftime("%Y-%m-%dT%H:%M:%S%z")

#fields_startup = startup.split('|')
#print(fields_startup)

fields_down = down.split('|')

#filename = '/var/log/modem_downstream.log'
filename = 'C:\Transient\scripts\output\modem_downstream.log'
file = open(filename, 'a')
#file.write('_time,channel,status,modulation,channel_id,frequency,power,snr,correctables,uncorrectables\n')

count = fields_down[0]
count_int = int(count)

i = 1
x = 1
while i <= count_int:
        y = x+9
        channel = ','.join(fields_down[x:y])
        file.write(now + ',' + channel + '\n')
        x = y
        i += 1

file.close()


fields_up = up.split('|')

#filename = '/var/log/modem_upstream.log'
filename = 'C:\Transient\scripts\output\modem_upstream.log'
file = open(filename, 'a')
#file.write('_time,channel,status,type,channel_id,rate,frequency,power\n')

count = fields_up[0]
count_int = int(count)

i = 1
x = 1
while i <= count_int:
        y = x+7
        channel = ','.join(fields_up[x:y])
        file.write(now + ',' + channel + '\n')
        x = y
        i += 1

file.close()
