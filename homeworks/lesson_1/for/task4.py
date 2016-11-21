def main():
    n = int(input("Введите количество чисел: "))
    zero_count = 0
    for i in range(n):
        number = int(input("Введите " + str(i) + " число: "))
        if number == 0:
            zero_count += 1
    print("Количество нулей: " + str(zero_count))

if __name__ == '__main__':
    main()
