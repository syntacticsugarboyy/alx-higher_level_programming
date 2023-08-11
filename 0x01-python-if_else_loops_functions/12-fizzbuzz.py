#!/usr/bin/python3
def fizzbuzz():
    for fizz_loop in range(101):
        if fizz_loop % 3 == 0:
            print('Fizz', end='')
        elif fizz_loop % 5 == 0:
            print('Buzz', end='')
        elif fizz_loop % 3 == 0 and fizz_loop % 5 == 0:
            print('FizzBuzz', end='')
        else:
            print('{}'.format(fizz_loop), end='')
        print(' ', end='')
