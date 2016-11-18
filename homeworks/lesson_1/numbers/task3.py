print("Задачка по распределнею яблоков среди детей")
kids_count = int(input("Введите количество детей: "))
apple_count = int(input("Введите количество яблок: "))
apple_recieved = apple_count // kids_count
apple_in_reserve = apple_count % kids_count
if (apple_count > kids_count):
    print("Детей больше чем яблок")
    print("Мы решили не раздавать яблоки, а сделать яблочный пирог")
else:
    print("Каждый ребёнок получит по" + str(apple_recieved) + " яблок")
    print("В запасе останется " + str(apple_in_reserve) + " яблок")
