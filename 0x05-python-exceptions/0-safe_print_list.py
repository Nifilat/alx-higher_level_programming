#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            real_num += 1
        except (IndexError, ValueError, TypeError):
            break
    print()
    return(real_num)
