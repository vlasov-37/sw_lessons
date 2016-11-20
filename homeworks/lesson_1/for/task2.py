n = int(input("Введите N: "))
cube_sum = 0
for i in range(1, n+1):
    cube_sum += i * i * i
print ("Кубическая сумма = " + str(cube_sum))
