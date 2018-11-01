#!/usr/bin/env python2

import sys
import struct
import datetime
import os


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, time = struct.unpack("<LLL", data[0:12])

(author) = data[12:20]

(count) = struct.unpack("<L", data[20:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

if count <= 0:
	bork("Bad section count <= 0")

print("------- HEADER -------")
print("MAGIC: %s\n" % hex(magic))
print("VERSION: %d\n" % int(version))
print("TIME: %s\n" % datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'))
print("AUTHOR: %s\n" % author)
print("SECTION COUNT: %d\n" % count)
print("-------  BODY  -------\n\n")

length_of_sections = len(data) - 24
offset = 24 
section_count = 0
while length_of_sections > 0:
	stype, slen = struct.unpack("<LL", data[offset:offset+8])
	offset = offset + 8
	section_count += 1
	if(stype == 0x1):
		f = open(os.getcwd()+"/" + sys.argv[1] + "png_" + repr(section_count) + ".png", 'wb')
		f.write("\211PNG\r\n\032\n")
		f.write(data[offset:offset+slen])
		f.close()
		print("PNG SECTION:\n Wrote to: " + os.getcwd()+"/" + sys.argv[1] + "png_" + repr(section_count) + ".png"+"\n")
	elif(stype == 0x2):
		if(slen%8 == 0):
			dwords = []
			for x in range(1,int(slen/8)+1):
				dword = struct.unpack("<Q", data[offset + (x-1) * 8:offset + x * 8])
				dwords.append(dword)
			print("DWORDS SECTION: \n" + repr(dwords) + "\n")
		else:
			bork("too many bytes")
	elif(stype == 0x3):
		(text) = data[offset:offset+slen]
		print("UTF-8 SECTION: \n%s\n" % text.decode('utf-8'))
	elif(stype == 0x4):
		if(slen%8 == 0):
			doubles = []
			for x in range(1,int(slen/8)+1):
				double = struct.unpack("<d", data[offset + (x-1) * 8:offset + x * 8])
				doubles.append(double)
			print("DOUBLES SECTION: \n" + repr(doubles) + "\n")
		else:
			bork("too many bytes")
	elif(stype == 0x5):
		if(slen%4 == 0):
			words = []
			for x in range(1,int(slen/4)+1):
				word = struct.unpack("<L", data[offset + (x-1) * 4:offset + x * 4])
				words.append(word)
			print("WORDS SECTION: \n" + repr(words) + "\n")
		else:
			bork("too many bytes")
	elif(stype == 0x6):
		if(slen == 16):
			(lat, lon) = struct.unpack("<dd", data[offset:offset+slen])
			print("COORDINATES SECTION:\nLatitude: %f , Longitude: %f\n" % (lat,lon))
		else:
			bork("Bad section length != 16")
	elif(stype == 0x7):
		if(slen == 4):
			(reference) = struct.unpack("<L", data[offset:offset+slen])
			if(reference < count and reference >= 0):
				print("SECTION REFERENCE: \n%d\n" % reference)
			else:
				bork("Bad section num. not in range")
		else:
			bork("Bad section length != 4")
	elif(stype == 0x9):
		(text) = data[offset:offset+slen]
		print("ASCII SECTION: \n%s\n" % text)

	offset = offset + slen
	length_of_sections -= 8+slen

print("ACTUAL SECTION COUNT:%d" % section_count)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!


