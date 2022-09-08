#!/usr/bin/python3
import sys
if __name__ == '__main__':
    str = 'arguments'
    str2 = 'argument'
    if len(sys.argv) == 1:
        print('0 {}.'.format(str))
    else:
        if len(sys.argv) == 2:
            str = str2
        print('{} {}:'.format(len(sys.argv) - 1,str))
        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, sys.argv[i]))
