#!/usr/bin/python3
''' Prints addition of integers '''
if __name__ == '__main__':
    import sys
run_sum = 0
for num in range(len(sys.argv) - 1):
    run_sum += int(sys.argv[num + 1])
print('{:d}'.format(run_sum))
