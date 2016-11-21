def main():
    print("Вычесление сколько прошло часов, минут и секунд по получению общего количечства секунд")
    time = int(input("Введите количество секунд прошедших с момента начала суток: "))
    hours = time // 3600
    minutes = time // 60 - hours * 60
    seconds = time - minutes * 60 - hours * 3600
    if hours >= 24:
        print("Вы ввели некорректное количество секунд")
        print("Прошло более суток!")
    else:
        print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

if __name__ == '__main__':
    main()
