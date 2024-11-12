import math

print("Задача 1")
num = list(map(int, input("Веддіть три числа:").split ()))
maxnum = max(num)
minnum = min(num)
print (f"min={minnum}, max={maxnum}")

print ("Задача 2")
length = int(6)
width = int(21)
area = width*length
print(f"Площа прямокутника: {area}")

print ("Задача 3")
number = int(13.3)
sqrt = math.sqrt(number)
number2 = round(sqrt, 2)
print (f"Квадратний корінь без округлення: {sqrt}, квадратний корінь округлений до двох знаків після коми: {number2}")