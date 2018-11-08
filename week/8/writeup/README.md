Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Andrew Wollack
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1.

Yes, conerstoneairlines.co

2. 

laz0rh4x and c0uchpot4doz

3.  

c0uchpot4doz : 206.189.113.189 from London

laz0rh4x : 104.248.224.85	3.429234	from north bergen new jersey

4.

2749

5.

1500 on October 25th

6.

https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7.

October 25th at 1500

To get all of this information I started to follow tcp streams until I found one that was human readable and in order to find out the traceroute command I looked at the ICMP packets

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1.

2018-10-24 20:40:07

2.

laz0rh4x

3.

Says that it has 9 sections actually has 11

4.

------- HEADER -------
MAGIC: 0xdeadbeef

VERSION: 1

TIME: 2018-10-24 20:40:07

AUTHOR: laz0rh4x

SECTION COUNT: 9

-------  BODY  -------


ASCII SECTION: 
Call this number to get your flag: (422) 537 - 7946

WORDS SECTION: 
[(3,), (1,), (4,), (1,), (5,), (9,), (2,), (6,), (5,), (3,), (5,), (8,), (9,), (7,), (9,)]

COORDINATES SECTION:
Latitude: 38.991610 , Longitude: -77.027540

SECTION REFERENCE: 
1

ASCII SECTION: 
The imfamous security pr0s at CMSC389R will never find this!

ASCII SECTION: 
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

COORDINATES SECTION:
Latitude: 38.991094 , Longitude: -76.932802

PNG SECTION:
 Wrote to: /Users/awollac/Documents/CMSC389R/389Rfall18/week/8/update.fpffpng_8.png

ASCII SECTION: 
AF(saSAdf1AD)Snz**asd1

ASCII SECTION: 
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9


DWORDS SECTION: 
[(4,), (8,), (15,), (16,), (23,), (42,)]

ACTUAL SECTION COUNT:11


 
 picture of an airplane with the flag CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}
 
 decode base 64 for CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}
 
diff checked the wikipedia entry on stegronography CMSC389R-{PlaIN_dIfF_FLAG}

5.

CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}

CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}

CMSC389R-{PlaIN_dIfF_FLAG}
