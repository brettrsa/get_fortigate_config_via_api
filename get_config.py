#!/usr/bin/python
#
# get info from fortigate device via api
#
# start
#

import requests

fortigate_host = 'ip:port'
fortigate_user = 'username'
fortigate_pass = 'password'

output = open('config', 'w')

login_url = 'https://%s/logincheck' % fortigate_host
login_payload = {'username': fortigate_user, 'secretkey': fortigate_pass}

r = requests.post(login_url, data=login_payload, verify=False)
cookiejar = r.cookies
csrftoken = r.cookies['ccsrftoken']

# this was tested on a 60D running 5.4.0GA
#r = requests.get('https://%s/api/v2/monitor/system/config/backup?destination=file&scope=global' % fortigate_host, cookies=cookiejar, verify=False)

# this was tested on on multiple models running code less than 5.4.0
r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

output.write(r.content)
output.close()

# end
