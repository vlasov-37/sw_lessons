def main():
    print("Больше предыдущего")
    s = input("Введите числа через пробел: ")
    a = s.split(" ")
    for i in range(1, len(a)):
        if (a[i] > a[i-1]):
            print(a[i], end=' ')
    print("")

if __name__ == '__main__':
    main()
