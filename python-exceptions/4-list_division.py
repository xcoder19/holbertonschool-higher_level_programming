#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            a = 0
        except ZeroDivisionError:
            print("Division by 0")
            a = 0
        except IndexError:
            print("Out of range")
            a = 0
        finally:
            result.append(a)
    return result