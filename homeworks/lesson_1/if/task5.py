print("Вывод минимального из 3 чисел")
a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
c = int(input("введите третье число: "))
if (a > b):
    min_number = b
else:
    min_number = a
if (c < min_number):
    min_number = c
print("Минимальное число: " + str(min_number))
