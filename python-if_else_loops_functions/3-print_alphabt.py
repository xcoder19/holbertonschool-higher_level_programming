#!/usr/bin/python3
a = 97
while (a <= 122):
    if ((chr(a) != 'q') and (chr(a) != 'e')):
        print("{:c}".format(a),end="")
    a = a+1
