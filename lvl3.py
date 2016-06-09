#! /usr/bin/env python3

# author:   Denisov Denis
# date:     08.06.2016
#
# Task (http://www.pythonchallenge.com/pc/def/equality.html):
# Level 3
#
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

filename = "equality"

import string

s_lowercase = set(string.ascii_lowercase)
s_uppercase = set(string.ascii_uppercase)



for line in open(filename):
    i = 0
    while True:
        try:
            if set(line[i] + line[i+4] + line[i+8]) < s_lowercase:
                if set(line[i+1:i+4] + line[i+5:i+8]) < s_uppercase:
                    print(line[i+4], end="")
                    i += 4
                    continue
            i += 1
        except IndexError:
            break

print("")
