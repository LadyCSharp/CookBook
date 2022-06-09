import requests
import pprint


token = '2ebabfea4958f5074f0399be90692e912238f43d'
headers = {'Authorization': f'Token {token}'}
# response = requests.get('http://127.0.0.1:8000/api/v0/ingredient/', headers=headers)
response = requests.get('http://127.0.0.1:8000/api/v0/ingredient/')
print(response.status_code)
pprint.pprint(response.json())
