from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

# headers = {
#     'username': 'elastic',
#     'password': 'YjhvfkmysqNfrjqGfhjkm'
# }

response = requests.put('http://192.168.10.10:5002/messages?pretty', auth=HTTPBasicAuth('elastic', 'YjhvfkmysqNfrjqGfhjkm'))
print(response)
print(response.content)