# Занятие 4
### Model View Controller концепция. Модели в django.
Решение домашнего задания.
[Основы проекта django](http://djbook.ru/rel1.9/intro/tutorial02.html)
На что обратить внимание:
 - Команды миграции перед началом работы. Основные команды django (makemigrations, migrate, sqlmigrate, check)
 - Модели это отображение классов в таблицы БД
 - коротко об атрибутах класса и атрибутах экземпляра класса
 - Инструментарий для просмотра БД sqlite (драйвер)
 - Заходим в shell проекта django
 - интерфейс администратора
[Типы полей django для моделей](http://djbook.ru/rel1.9/ref/models/fields.html) 
 
Домашнее задание.
 1. Создать виртуальное окружение для нового проекта. Установить туда django последней версии.
 1. Создать проект django и приложение командами startproject и startapp
 1. Сделать миграции, запустить пустой проект.
 1. Создать модель BlogEntry(name, text, author, date_create, date_modify), типы данных для полей задавать самостоятельно.
 1. Посмотреть вывод команд makemigraitons, sqlmigrate, migrate. Выполнить миграцию, добавить модель в админку.
 Для продвинутых
 1. Сделать простейшую view и шаблон, где будут отображаться записи.

### Ссылки
[Model-View-Controller](https://ru.wikipedia.org/wiki/Model-View-Controller)
[MVC это MTV в django](http://djbook.ru/ch05s02.html)
