#!/bin/env python2.7
# -*- encoding: utf-8 -*-

"""
Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
"""
import os
import transliterate


print transliterate.translit('Privet', 'ru')

ABS_PATH = '/home/g10k/git/sw_lessons/lessons/lesson_2/examples/transliaterate_dir'

def translitarate_dir(abs_path_to_dir, language='ru'):
    for file_name in os.listdir(abs_path_to_dir):
        abs_path_old = os.path.join(ABS_PATH, file_name)
        transliterated_file_name = transliterate.translit(file_name, language_code=language)
        abs_path_new = os.path.join(ABS_PATH, transliterated_file_name)
        os.rename(abs_path_old, abs_path_new)


# translitarate_dir(ABS_PATH)
translitarate_dir(ABS_PATH, language='en')