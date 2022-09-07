#!/usr/bin/python3
def uppercase(str):
    string=""
    for i in range(len(str)):
        if(str[i] >= 'a' and str[i] <= 'z'):
            string = string + chr((ord(str[i]) - 32))

    print("{}".format(string))


