Writeup 3 - OSINT II, OpSec and RE
======

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Wollack

## Assignment 3 Writeup

### Part 1 (100 pts)
Probably the most important vulnerability on the server was the fact that open ports could be accessed in order to log into the system. A whitelist should be put into the iptables of places that you would want to log into from so that intruders can't log on to your server from anywhere in the world. This would make it so that attackers of the system could not even see the open port unless they had a certain ip range that you own.(https://en.wikipedia.org/wiki/Whitelisting)

Additionally, the password strength of the server was far too weak. The server also used commonly known passwords that had been previously compromised. In the future you should use a password for your admin account and any other accounts on the machine that are generated and stored on your local computer that accesses the server. This is known as a password manager and allows you to have arbitrarily long and complicated passwords without having to remember them. This can easily prevent dictionary and word list attacks from ever occurring and would make brute-force attacks nearly impossible in a reasonable time span.(https://lifehacker.com/how-to-create-a-strong-password-1797681069)

Finally, an attacker should not be able to brute-force their way into your server and if they do you should know about it. To prevent this in the future you could use a few techniques including slowing down failed login attempts, locking accounts after too many attempts, remaking your passwords every month to two months, and using and Intrusion detection or prevention system to monitor your network traffic and notify the administrator during suspicious activity or access of sensitive files.(https://www.rapid7.com/fundamentals/brute-force-and-dictionary-attacks/)
