import requests

dn = '/restconf/data/Cisco-IOS-XE-native:native/interface/'
headers = {'Accept': 'application/yang-data+json'} # Header for the request, This key-value pair states that we want the request response to contain JSON data.
response = requests.get('https://10.254.0.1:443/' + dn,
    headers=headers,
    auth=('cisco', 'cisco'),
    verify=False)
data_dict = response.json() # call the request response opject method on the var response
#print(response.status_code)  # check the status of the code
#print(response.reason) # get more info about the status code
#print(response.content) # view the body of response 
print(data_dict)