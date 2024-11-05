import re

pattern = 'GigabitEthernet[1-4]'
interface = 'interface GigabitEthernet2 ip address 10.11.0.1 255.255.255.0'
result = re.search(pattern, interface)
print(result)