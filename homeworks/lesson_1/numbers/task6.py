def main():
    print("Вывод следущего и предыдещго числа")
    number = int(input("Введите число: "))
    next_number = number + 1
    prev_number = number - 1
    print("Следущее число: " + str(next_number))
    print("Предыдущее число: " + str(prev_number))

if __name__ == '__main__':
    main()
