#! /usr/bin/env python3

# author:   Denisov Denis
# date:     08.06.2016
#
# Task (http://www.pythonchallenge.com/pc/def/ocr.html):
# Level 2
#
# Recognize the characters that can be found in ocr file

filename = "ocr"

d = dict.fromkeys(map(ord,"!@#$%^&*()_+[]{}\n"),"")

for line in open(filename):
    print(line.translate(d), end="")

print("")
