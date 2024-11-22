import pandas 
import cisco


with open('router_info.csv', mode='r') as csv_file: #read data from a CSV file to a DataFrame, and print the DataFrame.
    df = pandas.read_csv(csv_file) 
# print(df)
# print(df['ip']) #print the op
# print(df.loc[[0]])#print the content of row 0

router_list = []
version_list = []

for index, row in df.iterrows():
    router = cisco.CiscoIOS(  
        row['ip'], 
        username=row['username'],  
        password=row['password'], 
        port=row['port'], 
        device_type=row['device_type'] 
    )
    version_data = router.get_IOS_version() 
    hostname = version_data['hostname'] 
    version = f"{version_data['rommon']} {version_data['version']}"

    router_list.append(hostname)
    version_list.append(version)

# print(router_list, version_list, sep='\n') # viewing the contents
router_data = pandas.DataFrame() # assign it the value of an empty DataFrame | starting this line write the code to a csv file
router_data['hostname'] = router_list # creating the column hostnam
router_data['version'] = version_list # creating the column version

# print(router_data)
router_data.to_csv('hostname_version.csv', index=False)