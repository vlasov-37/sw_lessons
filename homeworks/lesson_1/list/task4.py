import math

def sign(number:int):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
def main():
    print("Соседи одного знака")
    a = input("Введите числа через пробел: ")
    a = a.split(" ")
    i = 1
    while i < len(a):
        if sign(int(a[i])) == sign(int(a[i - 1])):
            print(a[i - 1], a[i])
            i += len(a) - i
        i += 1

if __name__ == '__main__':
    main()
