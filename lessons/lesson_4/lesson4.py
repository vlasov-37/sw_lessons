#/usr/local/env python
#

class Person(object):
    """ Комментарий
    """
    first_name = 'Александр' # Для всех экземпляров (shared переменная)
    last_name = 'Иванов'

    def __init__(self, last_name=None, first_name=None):
        if last_name:
            self.last_name = last_name
        if first_name:
            self.first_name = first_name

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name) # При получении self.attribute attribute сначала ищется в self потом в классе.



if __name__ == '__main__':
    print(Person.first_name)
    print(Person.last_name)
    default_person = Person()
    print(default_person)
    Person.last_name = u'Петров'  # Изменится у всех экземпляров класса, если они его не сохраняли "внутри себя"
    changed_person = Person()
    print(u'После изменения', default_person)
    print(u'После изменения', changed_person)

