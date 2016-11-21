def main():
    print("Последняя цифра числа")
    number = int(input("Введите число:"))
    print("Последняя цифра: " + str(number % 10))

if __name__ == '__main__':
    main()
