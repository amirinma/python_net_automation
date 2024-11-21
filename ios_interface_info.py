import class_and_inheritance
import sys
import os

# in below list of directories, python searches to import moduels 
# print(sys.path)

csr1kv1 = class_and_inheritance.CiscoIOS('10.254.0.1', username='cisco', password='cisco',
	         port=22, device_type='cisco_ios')
cwd = os.getcwd() + '/'
print(cwd)
router_dir = cwd + csr1kv1.hostname  + '/'
os.system('mkdir ' + router_dir)

interface_list = csr1kv1.get_interface_names()
datafile = f'{csr1kv1.hostname}_interfaces.txt'
with open(router_dir + datafile, 'w') as f:
     print(interface_list, file=f)