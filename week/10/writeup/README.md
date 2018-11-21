Writeup 10 - Crypto II
=====

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Andrew Wollack

## Assignment 10 Writeup

### Part 1 (70 Pts)

CMSC389R-{i_still_put_the_M_between_the_DV}

legit hash: 73a08cbb8734f643aeeb5cfba5905410

payload: Hello\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00malicious

fake_hash: b9d8192ba134c09017fbe631a06fc9c7

To solve this problem I essentially followed the powerpoint directly and varied the length of the message byte from 6-15. I had trouble figuring out how the message sent was supposed to be formatted until I realized that on the server side would be putting the secret before the message cahnging the length of the message.

### Part 2 (30 Pts)

gpg --decrypt ./message.private

gpg --gen-key

gpg -e -u "Andrew Wollack <andrew.wollack@gmail.com" -r "UMD Cybersecurity Club <president@csec.umiacs.umd.edu>" message.private


