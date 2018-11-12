Writeup 9 - Crypto I
=====

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Wollack

## Assignment 9 Writeup

### Part 1 (60 Pts)

In order to solve this part I wrote a script to take the hash of each salt and password possible and compare that hash to the list of possible hashes. Since the same text hashes to the same hash value it was trivial to find which salts and passwords were valid. I did initially have trouble since I didn't format the password properly to not include newlines but this was simple to fix.

Salt: k

Pass: neptune


Salt: m

Pass: jordan


Salt: p

Pass: pizza


Salt: u

Pass: loveyou



### Part 2 (40 Pts)

In order to solve this one I looked at the output for each question and used regex to reliably do the different types of hashes since the text was in the same format every time. I used an eval statement to compute the hash so that I could put in the different hash types as the hashlib method


=========================================

Hello there! Welcome to my hash workshop.

=========================================

Find me the sha224 hash of GIJabkIzKY
>>> 
3d94b6ab78f1ea75e65c2b48cc3b2fde6c941b6d77c599b23d1df34a

Correct!
Find me the md5 hash of 6pbemX4YnI
>>> 
16a6f18bab64f531d4b4bcfd7004abb8

Correct!
Find me the md5 hash of 5oQ4kagnBX
>>> 
abad432741b573403cb37891ffd8ee5e

Correct!
Find me the md5 hash of 32HicrvOci
>>> 
baa35af8bbc3b3c1474410347005d599

Correct!
Find me the md5 hash of omOLC4t5rk
>>> 
cfc65a8c56f7e379e7169e52df9c6a94

Correct!
Find me the sha256 hash of 6gmKgIsOlk
>>> 
fc262a86405f12e9c68b094688943fdb8f3cf5a3b079851588aaba271e492639

Correct!
Find me the sha1 hash of 1WkrdqNJmx
>>> 
9b764b3b578d7ddba6bc1c0595dfe0645be8d12f

Correct!
Find me the sha1 hash of NVh1HvYWDt
>>> 
857330fabf07945391fbec5cebf19e93efde9163

Correct!
Find me the sha512 hash of t7lct93drj
>>> 
fcce4e35c1c88729acb4778fff61afbe30eb40251462c5c9f1d3966b2649b1183dbc88cfa8721f89eb7af422b1df7dc29967116a5b5646b6266a10281b815df8

Correct!
Find me the sha224 hash of xB6qNOAZdw
>>> 
9de8c79b3be6988f1ab6fb20910771c6b7b42d6407623350e01ce3c5

Correct!
1541997200
1541997200

You win! CMSC389R-{H4sh-5l!ngInG-h@sH3r}