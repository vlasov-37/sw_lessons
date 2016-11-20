import math


n = int(input("Введите n :"))
for i in range(1, n+1):
    step = ""
    for j in range(i):
        step += str(j+1)
    print(step)
