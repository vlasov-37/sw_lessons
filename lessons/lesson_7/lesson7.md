# Занятие 7
## Валидаторы форм, валидаторы Моделей. Процесс clean для полей и формы. Связи one2one, one2M, коротко про M2M.

### Валидаторы форм 
Валидаторы форм
Валидатор на размер числа, длину строки. Дату

### Валидаторы моделей
Тоже самое что для формы.

### Процесс clean для полей и формы.

### Связь one2one 
 - В каких случаях нужна. (отделить сущности друг от друга, не всегда имеется информация, и не держать пустые столбцы, слишком большие изменения)
 - добавить связь к person - паспорт.
 - показать как добавлять mysqldb в проект
 - рассказать про [on_delete](http://djbook.ru/rel1.9/ref/models/fields.html#ref-onetoone) (в Sqlite не работает on delete)
 - показать "эмуляцию" каскадного удаления
 - как реализуется в SQL 
 
 
### Связь one2M
 - добавление - и прочее, все аналогично one2one
 

## Домашнее задание.
  #### Валидаторы
  - Написать валидатор для Предложения. 
    - С большой буквы
    - в конце `.` `!` или `?`
  - Валидатор на число от -20до-10 или 10 до 20 одновременно
 
  #### MySQL
  Установить MySQL сервер.
  Установить pip install MySQL-python, убедиться что все хорошо.
  Создать проект с настройками под MySQL
          
  #### Ссылки 
 