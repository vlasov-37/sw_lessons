print("Отделение дробной части от числа")
number = float(input("Введите число с дробной частью: "))
number = number % 1
print("Дробная часть: " + str(number))
#В ходе обработки интерпретатором чисел, на выходе мы получаем немного искажённое число
#На данном этапе познания языка python я не вижу другого выхода, кроме того как округить число
#Или решением этой задачи через строки, но эта задача находиться в разделе вычеслений
print("Округление: " + str(round(number, 4)))