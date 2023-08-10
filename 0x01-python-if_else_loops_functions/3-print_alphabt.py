#!/usr/bin/python3
letters = ''
for letter in range(97, 123):
    if letter == 113 or letter == 101:
        continue
    else:
        letters += '' + chr(letter)
print('{}'.format(letters), end='')
