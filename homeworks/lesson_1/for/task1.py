def main():
    numbers_count = int(input("Введите количество чисел: "))
    sum_numbers = 0
    for i in range(numbers_count):
        sum_numbers += int(input("Введите " + str(i + 1) + " число: "))
    print(sum_numbers)

if __name__ == '__main__':
    main()
