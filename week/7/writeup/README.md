Writeup 7 - Forensics I
======

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Wollack

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG

2. Chicago Illinois, John Handcock Center

3. 2018:08:22 16:33:24Z

4. iphone 8

5. 539.5 m Above Sea Level

6. CMSC389R-{look_I_f0und_a_str1ng}

### Part 2 (60 pts)
In order to reverse engineer the binary I opened it in cutter and saw that there was a file name loaded into the local memory pointing to /tmp/.stego initially I didn't see the period so I thought that something was wrong, but I then remembered that in unix files are hidden by period, so I found the file. I used file to determine the type of the file and went on gary kessler in order to find the right header. I saw that the header and footer for the JFIF were incorrect and that that was the reason that the file could not be opened or read by steghide, so I downloaded a hex editor and corrected the header and footer to follow the JFIF format. I could then open the file and see that there was a picture of a staegosaurus in the image. I then tried a bunch of passwords relate to dinosaurs like steg, stegosaur, dinosaur and then finally stegosaurus. This produced the flag below:

CMSC389R-{dropping_files_is_fun}

In order to find the metadata for part one I used exiftool on the file  and then used strings on the image and found the flag by searching for the flag format.
