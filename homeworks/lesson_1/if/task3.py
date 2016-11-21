def main():
    print("Шахматная доска")
    x1 = int(input("x координата для первой клетки: "))
    y1 = int(input("y координата для первой клетки: "))
    x2 = int(input("x координата для второй клетки: "))
    y2 = int(input("y координата для второй клетки: "))
    a = (x1 + y1) % 2
    b = (x2 + y2) % 2
    if (a == b):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
