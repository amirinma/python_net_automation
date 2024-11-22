import argparse 
 

# parser = argparse.ArgumentParser() 

# parser.add_argument('--ip', type=str, help='IP address, SSH Endpoint' ) 
# parser.add_argument('--port', type=int, help='Port for connection') 
# args = parser.parse_args() 





parser = argparse.ArgumentParser(description="Displays user information.")
parser.add_argument("name", help="Enter the user's name")
args = parser.parse_args()
