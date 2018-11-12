#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder



# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase
count = 0

for salt in salts:
	wordlist = open("../probable-v2-top1575.txt", 'r')
	for word in wordlist:
		count = count + 1
		hashlist = open("../hashes", 'r')
		for hashitem in hashlist:
			if(repr(hashlib.sha512((salt + word).replace("\n", "")).hexdigest()) == repr(hashitem.replace("\n", ""))):
				print("Salt: " + salt)
				print("Pass: " + word)
print(count)
