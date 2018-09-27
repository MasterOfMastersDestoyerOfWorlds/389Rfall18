Writeup 3 - Pentesting I
======

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Wollack

## Assignment 4 Writeup

### Part 1 (45 pts)
CMSC389R-{p1ng_as_a_$erv1c3} is the flag that I found in the home directory of the server after gaining access through command injection. I knew that the problem had something to do with escaping, so I started to mess with the input that I gave the uptime server and then remembered that if you supply a ; into a bash line then you can execute multiple commands in one line. Initially, I was providing an IP address with the input, but I later realized that in order to speed up the process I could not provide and input and ping would not run, so jut a ; would suffice. I Then explored the file system in the home directory and found the flag and put it out to terminal using ;cd ./home;cat flag.txt. In order to fix this problem Fred could use regex in order to match the input of the user to an IP address. This would make it so that any other format aside from "^(\d+[.]){3}.\d+$" would be invalid and recognized as likely injected code. This is a very similar problem to sql injection which is why I knew that unprotected input can lead to issues like this one.

### Part 2 (55 pts)
In order to complete part two I first implemented the menu before the shell with a usage function that prints the help menu, and the shell and the quit functions that control the entry into the machine and the exit of the program. the hardest part of this code was the change directory function, because first You have to deal with multiple levels of a directory that can go forward or backward and second you have to make sure that the directory that you're changing to actually exists. Both of these problems were solved in the main python function of the program.  Additionally in writing the pull command I simply checked if the file existed, then if it did I ran cat on the file and put it to the new local file and If the file on the remote machine didn't exist I printed "remote-path not found". Executing each command was as simple as writing ;cd [directory];[command]\n to the socket and waiting first for the banner and then for the response.
