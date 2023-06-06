#!/usr/bin/python3
def fizzbuzz():
    output = ""
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            output += "FizzBuzz "
        elif number % 3 == 0:
            output += "Fizz "
        elif number % 5 == 0:
            output += "Buzz "
        else:
            output += str(n) + " "
    print(output, end="")
