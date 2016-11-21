def main():
    print("Больше своих соседей")
    a = input("Введите числа через пробел: ")
    a = a.split(" ")
    i = 1
    while i < len(a) - 1:
        if (int(a[i]) > int(a[i - 1]) and int(a[i]) > int(a[i + 1])):
            print(a[i])
        i += 1

if __name__ == '__main__':
    main()
