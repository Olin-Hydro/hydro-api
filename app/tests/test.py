# File used for misc api testing
import requests


ph_log = {'ph': 11, 'ph_raw': 'testing data'}
headers = {'content-type': 'application/json'}

base_url = 'http://127.0.0.1:5000/ph'

r_all = requests.get(base_url)
r_1 = requests.get(base_url + '/2')
r = requests.post(base_url, json = ph_log, headers=headers)


print(r_all.content)
print(r_1.content)
print(r.content)