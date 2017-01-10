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

r = requests.get('https://%s/api/v2/monitor/system/config/backup?destination=file&scope=global' % fortigate_host, cookies=cookiejar, verify=False)

output.write(r.content)
output.close()

# end
