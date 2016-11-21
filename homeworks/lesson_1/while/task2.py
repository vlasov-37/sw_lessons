def main():
    print("Минимальный делитель")
    number = int(input("Введите число: "))
    divider = number
    min_divider = number
    while number // divider < number:
        if number % divider == 0:
            min_divider = divider
        divider -= 1
    print (min_divider)

if __name__ == '__main__':
    main()
