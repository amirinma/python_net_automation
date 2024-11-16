import re

pattern = 'GigabitEthernet[1-4]'
interface = 'interface GigabitEthernet2 ip address 10.11.0.1 255.255.255.0'
result = re.search(pattern, interface)
print(result)



pattern1 = 'programing language[1-5]'
information = 'Python is great programing language35!. Java is not a great programing language. Language'
info_result = re.search(pattern1, information)
# print(info_result)
# period . matches any character beside a new line
dot_reg = 'p........g'
dot_reg_exp = re.search(dot_reg, information)
# print(dot_reg_exp)
# [1-9][0-9] matches 10 - 99 
num_reg = '[0-9][1-9]'
num_reg_exp = re.search(num_reg, information)
# print(num_reg_exp)

# '$'
dol_sign = "guage$"
dol_sign_exp_info = "JavaScript is great programming language"
dol_sign_exp = re.search(dol_sign, dol_sign_exp_info)
if dol_sign_exp:
    print("Yes, the string ends with 'guage'")
else:
    print("no match found")


# Caret ^
caret_sign_exp = re.search('^Py', information)
if caret_sign_exp:
    print('Sting starts with -Py-')
else:
    print('String not matched.')


# zero or more occurence 
oc_pat = 'language*'
oc_pat_exp = re.search(oc_pat, information)
# print(oc_pat_exp)

# =========================> concatination 
# var = re.split(r'\n', data)    can be used to split data
int_data = [
'Interface              IP-Address      OK? Method Status                Protocol', 
'GigabitEthernet1       10.25.0.2      YES NVRAM  up                    up      ', 
'GigabitEthernet2       10.12.0.1       YES NVRAM  up                    up      ', 
'GigabitEthernet3       10.13.0.1       YES NVRAM  up                    up      ', 
'GigabitEthernet4       10.254.0.1      YES NVRAM  up                    up      '
]
# print(int_data)
ip_list = str()
# regex_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'     # it can match up any ip
regex_pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])' # spesific for ipv4
for value in int_data:
    # print(value)
    ip = re.search(regex_pattern, value)
    if ip:
        # print(ip)
        ip_list += ip.group(0) + ','
print(ip_list)
# =========================> extracting spesific string from string 
# for val in int_data:
#     ip = re.findall(r'\w+\s+([\d\.]+)', val)
#     print(ip.group(0))

data = 'GigabitEthernet1   ip_address  yes up  up GigabitEthernet2   ip_address  yes up  up GigabitEthernet3   ip_address  yes up  up '
re_pattern = r'(GigabitEthernet.*)'
# gigabit_ethernet_1 = re.search(re_pattern, data)

int_gig = re.search(re_pattern, data)
print(int_gig.groups(1))

