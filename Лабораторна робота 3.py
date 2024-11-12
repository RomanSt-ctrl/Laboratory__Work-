print ("Задача 1")
try:
    n = int(input("Ведіть число "))
    s = int(input("Ведіть cтепінь "))
    r = n**s
    print (r)
except ValueError:
    print ("введіть коректне число")
finally:
    print ("The end")

print ("Задача 2")
try:
    n = int(input("Ведіть число "))
    s = int(input("Ведіть cтепінь "))
    r = n+s
    print (r)
except ValueError:
    print ("введіть коректне число")

print ("Задача 3")
try:
    n = int(input("Ведіть число "))
    s = int(input("Ведіть cтепінь "))
    r = n/s
    print (r)
except ValueError:
    print ("введіть коректне число")
except ZeroDivisionError:
    print ("Ділення на нуль неможливе")