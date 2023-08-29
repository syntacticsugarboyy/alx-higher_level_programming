#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print('{:d}'.format(value))
            return True
    except Exception as err:
        import sys
        print('Exception: {}'.format(err), file=sys.stderr)
        return False
