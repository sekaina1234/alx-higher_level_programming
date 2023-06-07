#!/usr/bin/python3
j = 0
for d in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(d - j)), end="")
    j = 32 if j == 0 else 0
