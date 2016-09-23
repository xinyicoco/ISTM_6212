#!/usr/bin/env python

"""
    A filter that transform to lower case.
    """

import fileinput


def process(line):
    """For each line of input, _____."""
    #print(len(line))
    print(line.strip().lower())


for line in fileinput.input():
    process(line)
