import requests
import pprint
pp = pprint.PrettyPrinter(indent=2)

def callback(r, *args, **kwargs):
    print(r.url)
    print(r.status_code)

url = 'http://google.com'
response = requests.get(url, hooks=dict(response=callback))

if response.status_code == requests.codes.ok:
    print('status ok:', response.status_code)
else:
    print('status ng:', response.status_code)
