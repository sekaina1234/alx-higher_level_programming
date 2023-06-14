#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the set symmetric difference operation to find elements present in only one set
    only_diff = set_1 ^ set_2

    return only_diff
