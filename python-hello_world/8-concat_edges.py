#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[6].join([str.split(str[6])[5],str.split(str[6])[6],str.split(str[6])[12],str.split(str[6])[0]])
print(str)