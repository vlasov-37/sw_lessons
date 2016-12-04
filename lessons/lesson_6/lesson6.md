# Занятие 5
## Операции Queryset. Наследование шаблонов. Формы, задание параметров вручную, валидаторы

### Операции Queryset. 
Имеем класс Person из lesson4 приложения.

#### Создание объектов.
 ```p = Person(last_name=u'Власов', first_name=u'Сергей')``` # *Создает объект, можно изменить его, а потом вызвать save для сохранения. У `p` есть атрибут `p.pk`*
 
 `Person.objects.create(last_name=u'Власов', first_name=u'Сергей')` # *Создает и сохраняет объект сразу*
 
 
#### Получение объектов
 `Person.objects.all()` 
   - зачем objects, что это такое. Как создать другой менеджер queryset
   - как получить общее количество, разница между count() и len(qs) 
 
#### Другие операции с Queryset
 - .filter()
 - .exclude()
 - .filter()[:3]
 - .get()
 - .order_by('last_name')[0], ('last_name')[0]
 - lookups - фильтры полей (lte, gte,lt, gt, exact, iexact, contains, icontains)
 - Что такое lazy
 - update операция.
  
### Наследование шаблонов.

### Формы, задание параметров вручную, валидаторы

## Домашнее задание.
  
  Для модели:
  ```
  class Entry(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline
  ```
   
  Написать запросы:
   Вывести общее количество записей.
   Количество записей в 2016 году
   Запись с самым большим количеством комментариев.
   Запись с минимальным рейтингом.
   Первые 5 записей, отсортированные в алфавитном порядке.
   Первую по алфавиту запись.
   Исключить записи с n_pinbacks меньше 10
  
  В рабочем проекте из shell:
      создать запись в БД 2 способами.
      обновить значения через update 
 ## Ссылки 
 [Операции Queryset](http://djbook.ru/rel1.9/topics/db/queries.html) 