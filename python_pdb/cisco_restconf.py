import json
import json
import os
import requests
import pandas

DASH = '-' * os.get_terminal_size().columns # containing several dashes equal to the width of the terminal
conn_info = pandas.read_csv('conn_info.csv') #open csv file, define the varialbe conn_info as a pandas DataFrame object

for index, row in conn_info.iterrows(): # iterate throught the conn_info, find the appropriate value for ip, username and password
    # import pdb; pdb.set_trace() # halt the script's normal execution and break into the python debugger.
    ip = row['ip']
    username = row['username']
    password = row['password']
    uri = f'https://{ip}:443/restconf'
    auth = (username, password)

    response = requests.get(uri, auth=auth, verify=False) # making getrequest to the endpoint stored in uri
    print(response.content) #print the json response interpreted as a python dictionary to the terminal
    print(DASH)
