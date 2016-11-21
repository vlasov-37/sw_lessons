import math

def main():
    print("Задача по нахождению количества парт исходя из числа учеников")

    class_1 = int(input("Введите количество учащихся в первом мат-классе: "))
    class_2 = int(input("Введите количество учащихся в втором мат-классе: "))
    class_3 = int(input("Введите количество учащихся в третьем мат-классе: "))

    students_count = class_1 + class_2 + class_3
    tables_count = math.ceil(students_count / 2)

    print(str(tables_count) + " парт надо закупить!")

if __name__ == '__main__':
    main()
