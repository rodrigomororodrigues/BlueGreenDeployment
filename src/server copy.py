# sample python program for gethostname

import socket


# Get the local host name

myHostName = socket.gethostname()

print("Name of the localhost is {}".format(myHostName))

 
# Get the IP address of the local host

myIP = socket.gethostbyname(myHostName)

print("IP address of the localhost is {}".format(myIP))