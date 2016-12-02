#!/bin/env python2.7
# -*- encoding: utf-8 -*-

"""
Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
"""

def union_lists(list_one, list_two):
    return set(list_one) & set(list_two)


