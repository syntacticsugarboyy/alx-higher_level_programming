#!/usr/bin/python3
for digits in range(100):
    if digits < 99:
        print('{:02d}, '.format(digits), end='')
    else:
        print('{}'.format(digits))
