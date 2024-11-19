# Задача 1
def babble(arr):
    n =  len(arr)
    lichilnik = 0
    print (arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            lichilnik += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

    print ("Відсортований масив:", arr)
    print ("Кількість ітерацій:", lichilnik)

arra = [54, 94, 26, 12, 23, 11, 89] 
babble (arra)

# Задача 2
def Selec_sor(array, size):
    for i in range(size):
        min_in = i

        for j in range(i + 1, size):
            if array [j] < array[min_in]:
                min_in = j
        (array[i], array[min_in]) = (array[min_in], array[i])
        print (array)

arr = [-2, 45, 0, 11, -988, -97, -202, 747]
size = len(arr)

Selec_sor(arr, size)

