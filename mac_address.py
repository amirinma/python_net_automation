import re
import netmiko
import change_mac_notation
# read MAC address and store it as a string 
mac_list = re.findall(r'((?:[0-9a-f]{4}\.){2}[0-9a-f]{4})', show_arp)

# manipulate and concatinate MAC with reGex
mac_add = '000c.29e1.82c5'
print(change_mac_notation.change_notation(mac_add, ':'))

# convert EUI48 to EUI64
print(eui48to64.convert(mac_list))