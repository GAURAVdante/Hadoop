#!/usr/bin/env python
import sys
#empty dictinary wordcount
word2count = {}
# input comes from STDIN
for line in sys.stdin:
    #remove leading and trailing whitespaces
    line = line.strip()
    #parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    #convert count (current a string) to int
    try:
         count = int(count)
    except ValueError:
         continue
    try:
         word2count[word] = word2count[word]+count
    except:
         word2count[word] = count
#write the tuple to stdout
#note:they are unsorted
for word in word2count.keys():
    print '%s\t%s' %(word, word2count[word])
