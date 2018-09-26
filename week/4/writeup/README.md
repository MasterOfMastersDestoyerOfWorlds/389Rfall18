Writeup 3 - Pentesting I
======

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Wollack

## Assignment 4 Writeup

### Part 1 (45 pts)
CMSC389R-{p1ng_as_a_$erv1c3}
I knew that the problem had something to do with escaping, so I started to mess with the input that I gave the uptime server and then remembered that if you supply a ; into a bash line then you can execute multiple commands in one line, so I explored the file system in the home directory and found the flag and put it out to terminal using ;cd ./home;cat flag.txt

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
