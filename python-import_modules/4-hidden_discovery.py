#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    arr = dir(hidden_4)
    for str in arr:
        if str[0:2] != "__":
            print(str)
