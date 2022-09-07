#!/usr/bin/python3
a=0
while(a<=99):
    if (a >=0) and (a<10) and (a!=99):
       print(f"0{a}",end=", ")
    elif(a==99):
        print(f"{a}",end="")
    else:
       print(f"{a}",end=", ")
    a=a+1