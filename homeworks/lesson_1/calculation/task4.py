def main():
    print("Отделение дробной части от числа")
    number = float(input("Введите число с дробной частью: "))
    number = number % 1
    print("Первое число после точки: " + str(int(round(number, 1) * 10)))
    
if __name__ == '__main__':
    main()
