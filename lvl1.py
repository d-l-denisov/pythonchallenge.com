#! /usr/bin/env python3

# author:   Denisov Denis
# date:     06.06.2016
#
# Task (http://www.pythonchallenge.com/pc/def/map.html):
# Level 1

msg_original = list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
                    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

msg_copy = list.copy(msg_original)

# First solution

for i in range(len(msg_copy)):
    if msg_copy[i] not in ".' ()":
        msg_copy[i] = chr(97 + ((ord(msg_copy[i]) - 95) % 26))
print("".join(msg_copy))

# Second solution

import string

t = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print(("".join(msg_original)).translate(t))

print("map".translate(t))

