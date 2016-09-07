#!usr/bin/env python3
##################################################################
# CS483/583 Homework 1: Shift Cipher Decryption
##################################################################

from collections import Counter    # letter distribution dict
import os
import socket
from sys import platform as Platform
from string import ascii_lowercase
#from msvcrt import getch    # Press any key to exit.



#DIST:
#
#This function counts how many times each character appears in the text and then finds its distribution by dividing over the total number of characters
#
#Note, these are indexed by letter:frequency

def dist(t):
    count = {}
    for s in t:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
#    del count['']                   #this exists because we had a few extra '' characters floating around
#    print (count)

    totlett = 0

    for letter in ascii_lowercase:
        totlett = totlett + count[letter]

    for letter in ascii_lowercase:
        count[letter] = count[letter]/totlett

#    print (count)

    return count


#CALCDIST:
#
#This function takes the frequencies given by the text file and the calcuated frequencies (both indexed by letter:frequency) and multiplies them
#by index. Since multiplying (given * given) allows us to get the desired distribution, (given * shifted to match) will be equal to (given * given)
#
#This function multiplies them (a*a, b*b, etc) by iterating through ascii_lowercase.

def calcdist(givenfreq, calcfreq):
    totfreq = 0.0

    for letter in ascii_lowercase:
        sq = float(givenfreq[letter]) * float(calcfreq[letter])
        totfreq = totfreq + sq
    return totfreq


#SHIFTLETTER
#
#This function takes a dictionary indexed by letter:frequency and scoots each frequency forward by 1. It does so by keeping track of the "last"
#letter/index, copying the current one inserting the last one, and then keeping the current one as the last one.


def shiftletter(letterdict):

#    for letter in ascii_lowercase:
#        print(letter, letterdict[letter])
    
#    print(letterdict)
    last = letterdict['z']

#    print("\n")
#    print("\n")
#    print("\n")
    
    for letter in ascii_lowercase:
        temp = letterdict[letter]
        letterdict[letter]=last
        last = temp

#    for letter in ascii_lowercase:
#        print(letter, letterdict[letter])
        
#    print(letterdict)

    return letterdict
        


#SOLVE
#
#Iterates from 0 to 26, shifting the values up by 1 space each time, then calculates the distribution and compares. If found, prints the
#solution in a sentence format, showing how many times the letters have been shifted.

def solve(afterdist, distribs, current, goal):

    for i in range(0,26):
        afterdist = shiftletter(afterdist)
        current = calcdist(distribs,afterdist)

        if (current == goal):
            print("Solved! This cipher has been shifted by:")
            print('{} or {}, depeinding on whether you are sliding forwards or backwards.'.format(i,26-i))
            break
    return
    










text = []

###### Read the ciphertext into a list. ##
with open("shift-enc.txt") as f1:
    for word in f1:
        for char in word:
            char = char.rstrip('\n')
            text.append(char)


distribs = {}
        
###### Read the distribution file and store the dist for later. ##
with open("shift-freq.txt") as f2:
    for line in f2:
        werds = line.split(",")
        lettdis=werds[1].rstrip('\n')
        distribs[werds[0]] = float(werds[1])

#print(distribs)

######Printing goal and current distributions

goal = calcdist(distribs,distribs)

print("\n")
print("Goal:")
print(goal)
print("\n")

afterdist = dist(text)
current = calcdist(distribs,afterdist)
print("Starting value:")
print(current)
print("\n")

solve(afterdist, distribs, current, goal)
