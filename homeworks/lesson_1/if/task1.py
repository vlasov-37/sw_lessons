def main():
    print("Нахождение минимального из двух чисел")
    a = int(input("Введите 1-ое число: "))
    b = int(input("Введите 2-ое число: "))
    if (a < b):
        print("Минимальное число: " + str(a))
    else:
        print("Минимальное число: " + str(b))

if __name__ == '__main__':
    main()
