#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for dict_v in list_keys:
        if value == a_dictionary.get(dict_v):
            del a_dictionary[dict_v]

    return (a_dictionary)
