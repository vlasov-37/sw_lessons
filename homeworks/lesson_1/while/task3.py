def main():
    print("Степень двойки")
    number = int(input("Введите число: "))
    power = 0
    power_2 = 1
    while power_2 * 2 < number:
        power_2 = power_2 * 2
        power += 1
    print(power, power_2)

if __name__ == '__main__':
    main()
