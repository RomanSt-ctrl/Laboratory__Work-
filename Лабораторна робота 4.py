

print ("Задача 1")
def function (numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
eny_input = input("Введіть список чисел: ")
numbers = list(map(int, eny_input.split()))
result = function(numbers)
print("Добуток чисел:", result)

print ("Задача 2")
def function (numbers):
    product = 0
    for num in numbers:
        if num % 2 != 0:
            product += num
    return product
eny_input = input("Введіть список чисел: ")
numbers = list(map(int, eny_input.split()))
result = function(numbers)
print("Добуток чисел:", result)

print ("Задача 3")

i1 = int(input("Введіть число 1:"))
i2 = int(input("Введіть число 2:"))

def calc  (i1, i2):

    arifmetic = (i1 + i2)/2
    kvadratic = (i1 **2 + i2**2) /2
    return arifmetic, kvadratic

result = calc  (i1, i2)
print (result)