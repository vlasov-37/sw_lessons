def main():
    n = int(input("Введите количество карточек: "))
    sum_numbers = n
    for i in range(n):
        sum_numbers += (i + 1)
    for i in range(n):
        number = int(input("Введите номер " + str(i + 1) + "карты: "))
        sum_numbers -= number
    print("Пропавшая карта имеет номер: " + str(sum_numbers))

if __name__ == '__main__':
    main()
