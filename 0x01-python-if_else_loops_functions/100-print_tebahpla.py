#!/usr/bin/python3
j = 0
for d in range(ord('z'), ord('a') - 1, -1):
    if j == 0:
        print(chr(d).lower(), end="")
    else:
        print(chr(d).upper(), end="")
    j = 1 - j
