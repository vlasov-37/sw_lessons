def main():
    number = int(input("Введите число: "))
    i = 1
    while i ** 2 <= number:
        print(i ** 2)
        i += 1

if __name__ == '__main__':
    main()