Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 2 writeup

### Part 1 (45 pts)

1. FRED KRUEGER

2. 
https://stwity.com/kruegster1990/ twitter handle

http://www.cornerstoneairlines.co/about.html from twitter

https://pbs.twimg.com/profile_images/1028771026815995904/BVJ1ed66_400x400.jpg

kruegster@tutanota.com

Owns cornerstoneairlines

@kruester1990 instagram lookup

I really just googled the username and then looked at what sites he was one and then looked on big sites like facebook and instagram


3. 
142.93.118.186 reverse dns lookup

I took the website and put it into a reverse dns lookup cause i needed the ip and had the domain


4. 
User-agent: *

Disallow: /secret

CMSC389R-{fly_th3_sk1es_w1th_u5}

I followed the steps described in class and on the powerpoint


5. 
http://142.93.117.193/ admin page on company site 

just clicked through the site

6. 
canada and north america dnsdumpster

I followed the steps described in class and on the powerpoint

7. 

running ubuntu according to mxtoolbox and ssh banner

I tried to use nmap for this, but it wasn't plausible what the os was, so I just looked at the ssh banner and confirmed it with mxtoolbox.

8. *(BONUS)*

flag in dump textfiles: CMSC389R-{dns-txt-erc0rd-ftw}

homepage source
CMSC389R-{h1dden_fl4g_in_s0urce}

### Part 2 (55 pts)

nmap

PORT      STATE SERVICE

80/tcp    open  http

1337/tcp  open  waste

2222/tcp  open  EtherNetIP-1

10010/tcp open  rxapi

Username: kruegster

Password: pokemon

CMSC389R-{c0rn3rstone-air-27670}

So in order to solve this challenge I first googled the username to find out what kind of accounts that the person had and if I could associate the account with a name. I then used some of the tweets to locate where Fred worked and some of the tools from class in order to find out more about the website that he owns. I then nmapped the two different ip addresses that where available. I tried for a while to login via one of the ssh open ports, but I figured out that I needed to do a more exhaustive nmap, so I re-nmapped the sites with -p- and found the correct port. I then wrote the python brute force code and got the password. I then couldn't figure out which flight was the correct flag, so I look more into social media and other accounts with the same name and found a picture of his ticket and got the right flag.
