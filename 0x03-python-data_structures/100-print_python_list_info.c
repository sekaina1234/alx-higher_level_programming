#!/usr/bin/python3
def print_python_list_info(p):
    size = len(p)
    alloc = p.__alloc__()

    print("[*] Size of the Python List =", size)
    print("[*] Allocated =", alloc)

    for i in range(size):
        print("Element", i, ":", type(p[i]).__name__)
