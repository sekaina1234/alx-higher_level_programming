#!/usr/bin/python3
for j in range(10):
    for i in range(j + 1, 10):
        print("{:d}{:d}".format(j, i), end=", " if j < 8 or i < 9 else "\n")
