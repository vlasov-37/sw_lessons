n = int(input("Факториал: "))
factor = 1
factor_sum = 0
for i in range(1, n+1):
    factor *= i
    factor_sum += factor
print ("Факториал " + str(n) + " = " + str(factor))
print ("Сумма факториалов : " + str(factor_sum))
