import re
import netmiko

ip_pattern = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}'
                            r'(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])') #Regex matches a valid IPv4

def validate_ip(s):
    if ip_pattern.match(s): # if the pattern matches on the string s
        return True
    return False # return False anytime the condition did not evaluate to True

def connect(ip, username, password): # does assertion test using validate_ip() and raise assertion error if the validation is False
    assert validate_ip(ip), 'Invalid IP Address'
    return netmiko.ConnectHandler(ip, username=username, # assertion test pass, return a connection to an appliance
	    password=password, device_type='cisco_ios')

def get_data(conn, command):
    router_output = conn.send_command(command)
    assert 'Invalid input' not in router_output, 'Invalid command: ' + command # 'Invalid input' shouldn't be in router output
    assert len(router_output) > 0, 'No output, check command: ' + command # check if the length is greater than zero
    return router_output # if both assertion pass, return router_output

csr = connect('10.254.0.1', 'cisco', 'cisco')
'''
Running this script provide not output of all assertions pass
It only gives output if any of them fails
'''
print(get_data(csr, 'show run | include hostname'))