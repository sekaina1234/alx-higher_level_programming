#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique values
    unique_values = set()

    # Iterate over each element in the list
    for num in my_list:
        # Add the number to the set if it's not already present
        unique_values.add(num)

    # Calculate the sum of unique values
    sum_unique = sum(unique_values)

    return sum_unique
