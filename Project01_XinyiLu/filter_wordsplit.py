#!/usr/bin/env python

"""
    A filter that splits a line into words.
    """

import fileinput
import re

def process(line):
    """For each line of input, _____."""
    """
    line = re.sub(r"\w*\d\w*", " ", line);
    line = line.strip()
    if(len(line) > 0):
        words = re.split('\W+', line)
        for word in words:
            print(word)
    """
    #line = re.sub("^[0123456789]", " ", line)
    words = re.findall("\w{2,}", line)
    for word in words:
        if((word[0].isdigit()) == False):
            print(word)


for line in fileinput.input():
    process(line)
