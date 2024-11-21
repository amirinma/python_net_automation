import os
import requests

requests.packages.urllib3.disable_warnings()

test_uri = 'https://10.254.0.1:443/restconf/' # Representational State Transfer Configuration Protocol (RESTCONF)
dash = '-' * os.get_terminal_size().columns # print dashes as much as wide the terminal is
print(dash)

try:
    response = requests.get(test_uri, auth=('cisco', 'cisco'), verify=False)
    # print(response.status_code)
    response.raise_for_status() # rais the exception if the response is anything rather than 200
except requests.ConnectionError as error:
    output = error
except requests.HTTPError as error: # catch any httperror exception 
    output = error
else: # incase niether connectionerro nor httperror is raised, will the get the content of response 
    output = response.content
finally: 
    print(output)
    print(dash)