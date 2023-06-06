vi 3-print_alphabt.py
for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('q') and letter != ord('e'):
        print(chr(letter), end='')
