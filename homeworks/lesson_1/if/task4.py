print("Определение високосного года")
year = int(input("Введите год: "))
if (year % 4 and year % 100 == 0 or year % 400 and year % 100 == 0):
    print(str(year % 100))
    print("NO")
else:
    print("YES")
