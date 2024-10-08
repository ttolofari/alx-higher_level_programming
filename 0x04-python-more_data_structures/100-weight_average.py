#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    total_weighted_sum = sum(value * weight for value, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return (total_weighted_sum / total_weight if total_weight > 0 else 0)

