print("Задача 1")

num1 = int(input("Введіть число 1: "))
num2 = int(input("Введіть число 2: "))

if num1 == num2:
    print ("Числа співпадають")
elif num1 - num2 < 10:
    print ("Різниця менше 10")
else:
    print ("Різниця чисел більше ніж 10")

print ("Задача 2")

N = int(input("Введіть число: "))
print ("Таблиця квадратів")
for i in range(1, 11):
    n2 = N ** i
    print(f"{N}^{i} = {n2}")

print ("Задача 3")
nam = 3

while nam < 100:
    print (nam)
    nam = nam + 10

print (nam)