#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(str[6])[5] + str[6] + str.split(str[6])[6] + str[6] + str.split(str[6])[12] + str[6] + str.split(str[6])[0]
print(str)