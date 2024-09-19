#!/usr/bin/python3

def to_subtract(list_num):
    max_num = max(list_num)
    return max_num - sum(n for n in list_num if n < max_num)

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    rom_n = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    last_value = 0
    current_values = []

    for ch in roman_string:
        current_value = rom_n.get(ch, 0)
        
        if current_value == 0:
            continue
        
        if current_value <= last_value:
            total += to_subtract(current_values)
            current_values = [current_value]
        else:
            current_values.append(current_value)

        last_value = current_value

    total += to_subtract(current_values)

    return total

