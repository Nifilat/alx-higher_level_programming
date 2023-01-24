#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_num = 0
    for i in range(x):
        try:
            print("{:d}".format(int(my_list[i])), end="")
            real_num += 1
        except (ValueError, TypeError):
            continue
    print()
    return 
