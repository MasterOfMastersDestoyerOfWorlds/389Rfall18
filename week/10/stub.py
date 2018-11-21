#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import re

#####################################
### STEP 1: Calculate forged hash ###
#####################################

message = 'Hello'    # original message here

host = "142.93.118.186"   # IP address or URL
port =  1234    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data

s.recv(1024)

s.send('1\n')

s.recv(1024)

s.send(message + '\n')

data = s.recv(1024)

regex = re.search("Your hash: ([a-z0-9]*)", data)


legit = regex.group(1)     # a legit hash of secret + message goes here, obtained from signing a message


# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'malicious'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
for x in range(6, 16):
	s.send('2\n')
	s.recv(1024)
	s.send(fake_hash+'\n')
	print(s.recv(1024))
	message_length = len(message) + x
	padding =  "\x80" + "\x00"*((448-(8*message_length) - 1)/8)  + chr(message_length*8) + "\x00"*7
	# payload is the message that corresponds to the hash in `fake_hash`
	# server will calculate md5(secret + payload)
	#                     = md5(secret + message + padding + malicious)
	#                     = fake_hash
	payload = message + padding + malicious
	s.send(payload+'\n')
	s.recv(1024)

print(legit)
print(repr(payload))
print(fake_hash)
# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
