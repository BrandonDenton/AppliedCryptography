#!usr/bin/env python
##################################################################
# CS483/583 Homework 1: Shift Cipher Decryption
##################################################################

import os
import socket
from sys import platform as Platform
#from msvcrt import getch    # Press any key to exit.

text = []
found = 0		## flag for whether or not we've guessed the keyspace ##
sumdist = 0.0    # store sum of squares of probability of all characters

## Read the ciphertext into a list. ##
with open("shift-enc") as f1:
    while True:
        c = f1.read(1)
	if not c:
	    print "ciphertext reading complete"
            break
        text.append(c)
## Read the distribution file and store the dist's for later. ##
with open("shift-freq") as f2:
    for line in f2:
        werds = line.split()
        sumdist = sumdist + float(line[1])    # distribution for each letter is the second word of the line

## Shift all characters by n, then sum the squares of each ##
## character's distribution. If that sum roughly equals    ##
## 0.065, then assume you have found the shift factor that ##
## will produce the plaintext.                             ##
while(found == 0):
	i, j , k= 0, 0, 0    # incrementers, shift incrementer
	tryshift = []
	for i in text:
	    ## shift each character of text by k, then copy to tryshift ##
	    tryshift[i] = text[i] + k
	## calculate distribution for letters in the shifted text ##
	
	## if(memes > swag)
	##    me.append("succ")
	for j in tryshift:
        ## sum the square of each character distribution ##
