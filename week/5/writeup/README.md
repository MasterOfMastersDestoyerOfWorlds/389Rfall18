Writeup 5 - Binaries I
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION HERE*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 5 Writeup
Note: I compiled the assembly code with macho64 so that it could run on my mac, so If you want to compile it for ELF, first remove all of the underscores before the method names, and then remake the files without the macho64 argument in the yaml command.

In order to write this code I just coppied the provided C code and then rewrote every line into assembly and then added in the flags for the jumping logic. The second function was nearly identical to the first so I just coppied the first function and then made the necessary changes. Additionally, I could have just used the counter and added it to the string pointer in the mov statements, but I didn't feel like it and decided to just increment the pointers. The only issue that I ran into was that I was terminating the string because I used a full 64-bit register instead of a 8-bit register to change the characters in the first function. I just changed, the register size and fixed the issue. All of the registers that I used were caller saved, so I didn't need to store any of them on the stack.

