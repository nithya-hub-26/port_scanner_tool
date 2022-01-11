import pyfiglet
import sys
import socket
import datetime

# Starting Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

print("                                                                       ")
print(" #####################################################")
print(" #                                                   #")
print(" #                   Port scanner tool               #")
print(" #                                                   #")
print(" #####################################################")
print("                                                                        ")

# Defining a target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translate hostname to IPv4
else:
    print("Invalid amount of Arguments")
    print("Syntax: python port_scanner.py <ip>")

# Add pretty Banner
print("-" * 50)
print("Scanning Target: "+target)
print(f"Scanning started at: {str(datetime.datetime.now())}")
print("-" * 50)
print()

print("-" * 50)
start = int(input("Enter the starting port number: "))
end = int(input("Enter the ending port number: "))
print("-" * 50)

try:
    for port in range(start, end):  # max range of port is from 0 to 65535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program....")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\n Server not responding !!!!")
    sys.exit()
