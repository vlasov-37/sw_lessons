# Занятие 1
Установка virtualbox, python. Знакомство с github. Первые команды на python. Знакомство с основными типами данных, операторами Python.


Требования:
- ноутбук с ubuntu или установленной виртуальной машиной с ubuntu 
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
(venv) ~ pip install django
pip freeze # Смотрим какие пакеты стоят в текущем виртуальном окружении 
deactivate выходим из вирт. окружения
pip freeze Смотрим что тут django нету
```


 
### Знакомство с github.
1. Заходим на github.com, регистрируемся. Вас добавляю в соучастники проекта sw_lessons. 
2. Делаем clone sw_lessons. У каждого участника будет своя папка.
3. Создаем файл lesson_1.py в своей папке. Содержание (Привет, я такой то такой), я знаю Такие типы данных и операции с ними:
 - строки. Конкатенация, вывод, срез.
 - числа. Сложение, вычитание.
 - списки. Добавление нового элемента, извлечение. сложение, срезы
 - Операторы ветвления.
4. Запускаем, проверяем что работает делаем коммит и push в репозиторий. Просматриваем с сайта, что он появился.

Домашнее задание. Прочитать основные главы из некотрой книжки. Создать lesson1_homework.py файл С выводом прогноза погоды на следующую неделю

### Ссылки
[Инструкция](http://ru.wikihow.com/%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-Ubuntu-%D0%B2-VirtualBox)  как установить ubuntu на виртуальную машину Linux.

[Основные команды linux](http://forum.ubuntu.ru/index.php?topic=14535.15)

[Курс по git](https://githowto.com/ru)
