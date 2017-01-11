Download the config from a Fortigate via the API with python

Tested on various code versions and models, below is the url to use to grab the config, 

FortiGate-100D 5.0 GA           --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiGate-100D 5.0 GA Patch 9   --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiGate-100D 5.2.9GA          --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiGate-111C 5.0 GA Patch 14  --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiGate-111C 5.0 GA Patch 9   --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiGate-80C 5.2.5GA           --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiGate-80C 5.2.9GA           --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiWiFi-60C 5.0 GA Patch 9    --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiWiFi-60D 5.0 GA Patch 9    --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiWiFi-60D 5.2.4GA           --> r = requests.get('https://%s/downloadfile/sysconf.cfg?msg=1&CSRF_TOKEN=csrftoken&password=' % fortigate_host, cookies=cookiejar, verify=False) 

FortiWiFi-60D 5.4.0GA           --> r = requests.get('https://%s/api/v2/monitor/system/config/backup?destination=file&scope=global' % fortigate_host, cookies=cookiejar, verify=False)
