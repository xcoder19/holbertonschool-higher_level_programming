#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in (x):
            print("{}".format(my_list[i]), end="")
            count = count + 1
    except IndexError:
        pass
    finally:
        print()
        return count
