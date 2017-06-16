#!/usr/bin/env python
import sys
import csv
import re
# input comes from STDIN (standard input)
ctr = 0
for rw in sys.stdin:
    ctr = ctr + 1
    # remove leading and trailing whitespace
    # split theline into word
    # increase counters
    if ctr != 1:
            rw = re.sub(r'".*"','',rw)
            ct = 0
            words = rw.split(',')

            for word in words:
                word = word.strip()
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1
                ct = ct + 1
                if word:
                        if ct >= 25:
                                print '%s\t%s' %(word,1)
