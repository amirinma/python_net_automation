On line 8, type the following code to create a pointer to the list of dictionaries inside json_data.

interface_list = json_data['Cisco-IOS-XE-native:interface']['GigabitEthernet']
A pointer is an extra name that you can use to refer to an object that exists in memory. Because the list of dictionaries exists in memory, by simply assigning a variable, the value of that list will create a pointer. Using a pointer to manipulate data makes it easier to work with nested data or data within another object.

Once you convert JSON data to Python data types, you can add objects to a list, change the value of keys, or add new key-value pairs to a dictionary, and do anything else that you can do with Python data types.


On line 16, type the following code to convert the Python dictionary json_data, which contains all your JSON data, into a string containing formatted JSON using json.dumps().

formatted_json_data = json.dumps(json_data, indent=4)