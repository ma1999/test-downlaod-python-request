import requests


url = 'http://ipv4.download.thinkbroadband.com/512MB.zip'
r = requests.get(url, allow_redirects=True)

open('512.zip', 'wb').write(r.content)