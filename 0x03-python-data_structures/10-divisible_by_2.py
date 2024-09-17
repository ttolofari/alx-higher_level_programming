#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    output = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            output.append(True)
        else:
            output.append(False)
    return output
