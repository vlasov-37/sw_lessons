# Занятие 1
Знакомство с github. Знакомство с pip, virtualenv. Первые команды на python. Знакомство с основными типами данных, операторами Python. Обзор структуры проекта django.

```
python # мы попали в интерпретатор python >>> видим, версию 2.7.x или 3.5 на ubuntu 16.04. 
>>> exit() - выход из интерпретатора
apt-get install virtualenv python-pip
mkdir lesson1
virtualenv venv_python2.7
source venv_python2.7/bin/activate # Активируем виртуальное окружение, есть shortcut virtualenvwrapper сделать это командой короче.
python 
```
Выполняем команды из [руководства для новичков](http://pythontutor.ru/lessons/inout_and_arithmetic_operations/)

1. Переменные не строго типизированные
1. отличия python2.7 и python3
 1. ```from __future__ import absolute_import unicode_literals, print_function``` # Должно быть в начале файла
1. Отступы важны (tab или space, но не смешивать)

Устанавливаем django
```
source venv_python2.7/bin/activate 
(venv) ~ pip install django # Рассказать про версионирование пакетов.
pip freeze # Смотрим какие пакеты стоят в текущем виртуальном окружении 
deactivate выходим из вирт. окружения
pip freeze Смотрим что тут django нету

source venv_python2.7/bin/activate 
django-admin # Изучаем вывод команды
django-admin startproject first_project
Изучаем файлы  django проекта.
[Вводное описание django](https://tutorial.djangogirls.org/ru/django/)
```

### Ссылки

[Инструкция для отправки своего кода на github](https://github.com/g10k/sw_lessons/blob/master/lessons/lesson_1/install_and_commit_via_git.md)

[Инструкция](http://ru.wikihow.com/%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-Ubuntu-%D0%B2-VirtualBox)  как установить ubuntu на виртуальную машину Linux.

[Основные команды linux](http://forum.ubuntu.ru/index.php?topic=14535.15)

[Курс по git](https://githowto.com/ru)
