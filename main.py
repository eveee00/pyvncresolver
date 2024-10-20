import requests
r = requests.get('https://computernewb.com/vncresolver/api/scans/vnc/random')
print(r.text)