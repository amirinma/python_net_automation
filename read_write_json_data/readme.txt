On line 8, type the following code to create a pointer to the list of dictionaries inside json_data.

interface_list = json_data['Cisco-IOS-XE-native:interface']['GigabitEthernet']
A pointer is an extra name that you can use to refer to an object that exists in memory. Because the list of dictionaries exists in memory, by simply assigning a variable, the value of that list will create a pointer. Using a pointer to manipulate data makes it easier to work with nested data or data within another object.

Once you convert JSON data to Python data types, you can add objects to a list, change the value of keys, or add new key-value pairs to a dictionary, and do anything else that you can do with Python data types.


On line 16, type the following code to convert the Python dictionary json_data, which contains all your JSON data, into a string containing formatted JSON using json.dumps().

formatted_json_data = json.dumps(json_data, indent=4)


Notice that the function get_interface_info(), defined on line 48, is incomplete. On line 52, change the value of url_base to be 'https://' + self.ip + ':' + self.port.

This value will act as the API root for the requests. You will concatenate this string with the value dn to create a complete Uniform Resource Identifier (URI).

Type the following:

url_base = 'https://' + self.ip + ':' + self.port


On line 55, replace pass with the following line of code:

headers = {'Accept':'application/yang-data+' + data_type}
HTTP headers consist of key-value pairs, so when making a request with the requests module, headers will always be stored in a dictionary.



Beginning on line 56, type the following code to make a GET request to the endpoint uri using the instance variables defined on instantiation and the local variables created in the get_interface_info() function.

request_response = requests.get(uri,
   headers=headers, 
   auth=(self.username, self.password), 
   verify=False)


The function get_interface_ips() defined on line 63 requires an argument for the parameter interface_info. The value of this argument will be the data returned from the other class function, get_interface_info().

Create a variable named interface_dict that contains the value of the key 'Cisco-IOS-XE-native:interface' in interface_info. Create another variable named interface_list that contains value of the key 'GigabitEthernet' in interface_dict.

Beginning on line 67, replace the pass statement with the following code:

interface_dict = interface_info['Cisco-IOS-XE-native:interface']
interface_list = interface_dict['GigabitE

line 78: 
print(csr.get_interface_ips(csr.get_interface_info()))
This code has the main() function print the data returned from csr.get_interface_ips() using the dictionary returned from csr.get_interface_info() as the argument.
