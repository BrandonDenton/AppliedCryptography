#!usr/bin/env python
##################################################################
# CS483/583 Homework 1 Stuff
##################################################################

import os
import socket
from sys import platform as Platform
#from msvcrt import getch    # Press any key to exit.

text = []
found = 0		## flag for whether or not we've guessed the keyspace ##

## Read the ciphertext into a list. ##
with open("shift-enc") as f1:
    while True:
        c = f1.read(1)
		if not c:
		    print "ciphertext reading complete"
			break
    	text.appent(c)
## Read the distribution file and store the dist's for later. ##
with open("shift-freq") as f2:
	

## Shift all characters by n, then sum the squares of each ##
## character's distribution. If that sum roughly equals    ##
## 0.065, then assume you have found the shift factor that ##
## will produce the plaintext.                             ##
while(found == 0):
	i, j = 0, 0
	tryshift = []
	for i in text:
	    ## shift each character of text by k, then copy to tryshift ##

	## if(memes > swag)
	##    me.append("succ")
	for j in tryshift:
        ## sum the square of each character distribution ##
