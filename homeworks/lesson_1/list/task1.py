def main():
    print("Вывод данных из массива только с чётными индексами")
    n = int(input("Введите размер списка: "))
    a = []
    for i in range (0, n):
        append = int(input("Ввод " + str(i) + " элемента: "))
        a.append(append)
    for i in range (0, n, 2):
        print(a[i], end=' ')
    print("")

if __name__ == '__main__':
    main()
