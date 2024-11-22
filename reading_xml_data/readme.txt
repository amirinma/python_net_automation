Beginning on line 9, type the following code, indented four spaces so that it is in the get_interface_info() function. The first line of code defines a variable called api_root as a string containing the application programming interface (API) root Uniform Resource Identifier (URI). The next line defines another variable dn as a string containing the distinguished name of a managed object. You can combine the api_root with the distinguished name of a managed object to create an endpoint to which you can make requests and acquire interface data in XML format.

api_root = 'https://10.254.0.1:443/restconf' 
dn = '/data/Cisco-IOS-XE-native:native/interface/'

Beginning on line 16, within get_interface_info(), type the following code.. This conditional block will print the contents of response (using UTF-8 encoding) to the terminal if to_terminal=True or return the text contents of response if to_terminal=False.

if to_terminal == True:
    print(response.content.decode('utf-8'))  
else:
    return response.content


On line 2, import the class BeautifulSoup from the package bs4.
The BeautifulSoup class uses an XML parsing module to interpret XML data and creates an object that has methods that help you work with XML data.


On line 23, type the following code to interpret the data in xml_data with BeautifulSoup() using the lxml XML parser. A parser breaks data down into smaller elements so that the data can be translated from one language to another. The lxml parser makes it so the BeautifulSoup class can use XML data.

soup = BeautifulSoup(xml_data, 'lxml')



Instead of viewing the contents of one gigabitethernet tag, use the find_all() method to create a list of BeautifulSoup objects, each containing information pertaining to one interface. Comment out the print statement on line 24, and then on line 25, type the following code:

for intf in soup.find_all('gigabitethernet'): 
    print(intf) 
    print('-' * 50)



You cannot always use dot notation to find the data that you are looking for in an XML string using BeautifulSoup(). Sometimes, the name of a pre-existing method or attribute will conflict with the name of a tag. The BeautifulSoup() attribute name will always contain the name of the tag that you are viewing. In the XML interface data, name is also how you would distinguish the different GigabitEthernet interfaces. Instead, you can use the find() method, which will return a match, including the tags. Use the attribute string to find the data between the open and close tag.

Replace the line of code on line 26 with the following line of code, then save the script and run it in with the terminal command python cisco_restconf.py.

print(intf.name + intf.find('name').string)


Why line 28 , 29 are commented out:
Observe the contents of the tag <ip> in the following image. The tag <address> occurs two times in the path to the primary IP address of the interface.
<ip>
    <address>
        <primary>
            <address>
                10.254.0.1
            </address>
            <mask>
                255.255.255.0
            </mask>
        </primary>
    </address>
</ip>
When this is the case, dot notation or the find() method will each return the first tag that matches your search. GigabitEthernet 1 does not have an <ip> tag and will return None if you try to find it. You can return the result of soup.find('ip') to a variable, and use a conditional statement to do something if that tag is present.

Erase the code on lines 26 and 27. Beginning on line 26, indented to be in the for loop, type the following lines of code:

print('-' * 25)
ip = intf.find('ip')
if ip:
    print('GigabitEthernet', intf.find('name').string)  
    print(intf.ip.primary.address)