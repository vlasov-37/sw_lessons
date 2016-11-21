def main():
    print("Расчёт вклада под %")
    x = int(input("Введите начальный вклад: "))
    p = int(input("Введите проценты вклада: "))
    y = int(input("Введите ожидаемую сумму: "))
    year = 0
    while x < y:
        x += x * (0.01 * p)
        x = round(x, 2)
        year += 1
    print("Через " + str(year) + " лет на счете будет " + str(x) + " рублей")

if __name__ == '__main__':
    main()
