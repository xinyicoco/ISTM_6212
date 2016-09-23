#!/usr/bin/env python

"""
    A filter that removes stopwords.
    """

import fileinput
import re
stopwords = []

def process(line):
    line = line.strip();
    if(line not in stopwords):
        print(line)





for line in fileinput.input("stoppingwords.txt"):
    words = re.findall("\w{1,}", line)
    for word in words:
        stopwords.append(word)



for line in fileinput.input():
    process(line)
