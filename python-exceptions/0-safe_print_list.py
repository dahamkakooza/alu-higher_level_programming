#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count =
    try:
        for i in range(x):
            print(my_list[count], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
