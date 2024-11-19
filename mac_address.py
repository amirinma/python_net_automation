import re
import change_mac_notation
# read MAC address and store it as a string 
mac_list = re.findall(r'((?:[0-9a-f]{4}\.){2}[0-9a-f]{4})', show_arp)

mac_add = '000c.29e1.82c5'
print(change_mac_notation.change_notation(mac_add, ':'))