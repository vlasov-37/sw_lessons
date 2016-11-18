import math #I will use math module for my first script
#line comment
'''
Throuth liens comment
'''
print("Sup budy!") #default print function
print("My firstname is Nickolay, and the secondname is Metelev")
print("I'm student of MIREA Serpuhov's branch")
print("And this is my first python script :)")
print("What is your name?")
companion = input()
print("Sup " + companion + "!")
print("lets look some variable types: ")
number = input("type some number here: ")
print("Look some basic math operations in python:")
print("add: ")
print(number + " + 5 = " + str(int(number) + 5))
print("multiply: ")
print(number + " * 23 = " + str(int(number) * 23 ))
print("pow: ")
print(number + " ^ 3 = " + str(int(number) ** 3 ))
print("devision: ")
print(number + " / 2 = " + str(int(number) / 2 ))
print("int devide: ")
print(number + " \ 2 = " + str(int(number) // 2 ))
print("remainder of the devision: ")
print(number + " / 5, remainder: " + str(int(number) % 5 ))
print("Lets find some area of circle")
circle_radius = float(input("Input the radius (sm): "))
circle_area = math.pi * (circle_radius ** 2)
print("formula of cirlce area is (S = Pi * r ^ 2)")
print("Pi * " + str(circle_radius) + " ^ 2")
print("cirlce area : " + str(circle_area) + " (sm^2)")
