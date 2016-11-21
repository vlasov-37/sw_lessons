#!/bin/env python2.7
# -*- encoding: utf-8 -*-
# shebang - позволяет выполниться скрипту python без указания python script.py, а как ./script.py
"""В школе решили набрать три новых математических класса.
 Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и
 купить в них новые парты. За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом
 из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три
  натуральных числа: количество учащихся в каждом из трех классов.
"""

# Что будет если запустить с неверными параметрами.

FIRST_GRADE_CHILDRENS = 29
SECOND_GRADE_CHILDRENS = 18
THIRD_GRADE_CHILDRENS = 30
FOURTH_GRADE_CHILDRENS = 25
FIVES_GRADE_CHILDRENS = 31

ALL_GRADES_CHILDRENS = [
    FIRST_GRADE_CHILDRENS, SECOND_GRADE_CHILDRENS, THIRD_GRADE_CHILDRENS, FOURTH_GRADE_CHILDRENS, FIVES_GRADE_CHILDRENS
]


def get_school_desks_for_3_grades(first_grade, second_grade, third_grade):
    first_grade_desks_count = first_grade / 2 + 1
    second_grade_desks_count = second_grade / 2 + 1
    third_grade_desks_count = third_grade / 2 + 1
    desks_count = first_grade_desks_count + second_grade_desks_count + third_grade_desks_count
    return desks_count


def get_school_desks_for_any_grades_1(grades_list):
    desks_count = 0
    for grade in grades_list:
        desks_count += grade / 2 + 1
    return desks_count


def get_school_desks_for_any_grades_2(*grades):
    desks_count = 0
    for grade in grades:
        desks_count += grade / 2 + 1
    return desks_count


def get_shool_desks_for_any_grade_3(*grades):
    return sum([grade/2 + 1 for grade in grades])


if __name__ == '__main__':
    print get_school_desks_for_3_grades(FIRST_GRADE_CHILDRENS, SECOND_GRADE_CHILDRENS, THIRD_GRADE_CHILDRENS)
    print get_school_desks_for_any_grades_1(ALL_GRADES_CHILDRENS)
    print get_school_desks_for_any_grades_2(*ALL_GRADES_CHILDRENS)
    print get_shool_desks_for_any_grade_3(*ALL_GRADES_CHILDRENS)






