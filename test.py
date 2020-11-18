import requests

ph_log = {'ph': 5, 'ph_raw': 'test data'}

base_url = 'http://127.0.0.1:5000/ph'

r_all = requests.get(base_url)
r_1 = requests.get(base_url + '/1')
#r = requests.post(base_url, data = ph_log)


print(r_all.content)
print(r_1.content)
#print(r.content)