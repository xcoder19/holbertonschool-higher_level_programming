#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            del a
        except ZeroDivisionError:
            print("division by 0")
            del a
        except IndexError:
            print("out of range")
            del a
        finally:
            result.append(a)
    return result