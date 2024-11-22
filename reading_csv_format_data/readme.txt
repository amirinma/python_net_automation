On line 1 of your script, type the following code to import pandas, read data from a CSV file to a DataFrame, and print the DataFrame.

import pandas 

with open('router_info.csv', mode='r') as csv_file: 
    df = pandas.read_csv(csv_file) 
print(df)
A pandas.DataFrame object is a two-dimensional tabular representation of data with rows and columns, similar to an Excel spreadsheet.
The pandas module reads the data and displays it in a visually appealing way. The numbers to the left of the DataFrame are the index values of the rows.

Beginning on line 14, type the following code to create a for loop using two variables, index and row, to iterate df.iterrows():

for index, row in df.iterrows():
    router = cisco.CiscoIOS(  
        row['ip'], 
        username=row['username'],  
        password=row['password'], 
        port=row['port'], 
        device_type=row['device_type'] 
    )
The column names are used as a string within brackets after each row to return the value in each column. The values in each row are used to create an instance of cisco.CiscoIOS().


Beginning on line 22, within the for loop, indented four spaces, type the following code to acquire the formatted router output from the command sh version, using the method get_IOS_version().

	version_data = router.get_IOS_version() 
	hostname = version_data['hostname'] 
	version = f"{version_data['rommon']} {version_data['version']}"
The key 'hostname' is used to get the hostname, and the values of the keys 'rommon' and 'version' in an f-string are used to create a new string containing operating system and version data.

On line 35, type the code router_data.to_csv('hostname_version.csv', index=False) to write the DataFrame that you created to a CSV file, using the pandas DataFrame method to_csv().

This code calls to_csv() on the DataFrame object router_data. The argument 'hostname_version.csv' is the file that will be created and populated. You do not need the index values in your CSV file, so the value of the keyword index is set to False.
