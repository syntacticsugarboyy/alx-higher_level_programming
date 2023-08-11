#!/usr/bin/python3
for fir_dig in range(10):
    for sec_dig in range (fir_dig + 1,10):
        if fir_dig < 8:
            print('{}{}'.format(fir_dig, sec_dig), end=' ')
        else:
            print('{}{}'.format(fir_dig, sec_dig))
