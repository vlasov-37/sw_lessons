def main():
    print("Вывод данных из массива только с чётными элементами")
    n = int(input("Введите размер списка: "))
    a = []
    for i in range (0, n):
        append = int(input("Ввод " + str(i) + " элемента: "))
        a.append(append)
    for i in range (0, n):
        if (a[i] % 2 == 0):
            print(a[i], end=' ')
    print("")

if __name__ == '__main__':
    main()
