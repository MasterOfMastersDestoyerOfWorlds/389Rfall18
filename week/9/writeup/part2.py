#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port =  7331    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)

while(data!=""):

	print(data)

	regex = re.search("(\w{3}[0-9]*) hash of (\w*)", data)
	if regex is not None:
		message = eval("hashlib."+ regex.group(1) +"(\""+ regex.group(2) +"\").hexdigest()") + "\n"
		print(message)
		s.send(message)

	data = s.recv(1024)


# close the connection
s.close()
