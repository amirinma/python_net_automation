import re
data = "xyz785abc5xy2"
pattern = r'[abc][1-7]'
match = re.search(pattern, data)
print(match.group())