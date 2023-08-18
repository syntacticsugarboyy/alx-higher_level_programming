#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1
if num_args < 1:
    print('{:d} arguments.'.format(num_args))
elif num_args == 1:
    print('{:d} argument:'.format(num_args))
    print('{:d}: {}'.format(num_args, sys.argv[1]))
else:
    print('{:d} arguments:'.format(num_args))
    for args in range(1, num_args + 1):
        print('{:d}: {}'.format(args, sys.argv[args]))
