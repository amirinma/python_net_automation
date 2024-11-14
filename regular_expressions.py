import re

pattern = 'GigabitEthernet[1-4]'
interface = 'interface GigabitEthernet2 ip address 10.11.0.1 255.255.255.0'
result = re.search(pattern, interface)
print(result)



pattern1 = 'programing language[1-5]'
information = 'Python is great programing language35!. Java is not a great programing language. Language'
info_result = re.search(pattern1, information)
print(info_result)
# period . matches any character beside a new line
dot_reg = 'p........g'
dot_reg_exp = re.search(dot_reg, information)
print(dot_reg_exp)
# [1-9][0-9] matches 10 - 99 
num_reg = '[0-9][1-9]'
num_reg_exp = re.search(num_reg, information)
print(num_reg_exp)

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
oc_pat = 'language*2'
oc_pat_exp = re.search(oc_pat, information)
print(oc_pat_exp)
