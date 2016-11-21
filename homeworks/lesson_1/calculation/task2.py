def main():
    print("Длинна кольцевой дороги 109 km")
    v = int(input("Введите скорость: "))
    t = int(input("Введите время: "))
    path = v * t
    der = path // 109
    if (path > 0):
        path = path - 109 * der
    elif (path < 0):
        path = abs(abs(path) - 109 * abs(der))
    print("Пройденый путь: " + str(path))

if __name__ == '__main__':
    main()
