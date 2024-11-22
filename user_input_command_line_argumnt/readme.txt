for cisco > main fu:
The sys module contains the dynamic object argv, which is a list containing the command-line arguments following the python command. On the command line, if you were to type python example.py test1 test2, the list sys.argv would look like this: ['example.py', 'test1', 'test2']

On line 4, type import sys. Leave two lines of whitespace between this import and the next line of code.


Run the script with the terminal command python cisco.py 10.254.0.1. The list held by sys.argv that is created when you use this command looks like this: ['cisco.py', '10.254.0.1']. The code in the main() function is using the item at index value 1 of this list, '10.254.0.1', as the IP address for CiscoIOS().__init__().

cisco.py > line5> The argparse module enables you to use positional arguments and options when you run your script from the command line.


Use the following terminal command to run cisco.py. In this command, provide the IP address 10.254.0.1 as the positional argument ip. Next, use the optional arguments (also called options) --username and --password to pass in the value cisco for each. Finally, use the default values for the optional arguments port and device_type.

cli command: 
python cisco.py 10.254.0.1 --username cisco --password cisco