#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or str(roman_string) is False:
        return 0
    result = 0
    romman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
 }
    for x in roman_string:
        for i in romman:
            if (i == x):
                result = result + romman[i]

    if (len(roman_string) >= 2):
        if (roman_string != "III" and roman_string != "II" and roman_string[0] == 'I' and roman_string[1] != 'X' and roman_string[1] != 'V'):
            print('hello')
            result = result - 1

    if (len(roman_string) >= 2 and roman_string[0] == 'I' and roman_string[1] == 'X'):
        print('hello2')
        result = result - 2

   
    if (len(roman_string) >= 2 and roman_string[0] == 'I' and roman_string[1] == 'V'):
        print('hello3')
        result = result - 2
    print(result)
