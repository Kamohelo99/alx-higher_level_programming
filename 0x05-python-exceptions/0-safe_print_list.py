#!/usr/bin/python3

def safe_print_list(my_list= [], x=0):
    if not my_list:
        return 0
    counter = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter = counter + 1	
    except IndexError:
        pass

    return counter
