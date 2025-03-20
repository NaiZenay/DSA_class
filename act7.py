import sys
import random
import time

def bubble_sort(arr):
    print("Memorio usada antes del BubbleSort: "+str(sys.getsizeof(arr)))
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print("Memoria usada durante la iteracion: ("+str(j)+") del BubbleSort: "+str(sys.getsizeof(arr)))
        if not swapped:
            break
    print("Memorio usada al final de BubbleSort: "+str(sys.getsizeof(arr)))

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        print("Inicio:"+str(sys.getsizeof(arr)))
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        print("Medio:" + str(sys.getsizeof(arr)))
    print("fin"+str(sys.getsizeof(arr)))

def quick_sort(arr):
    print("Memoria usada al inicio: " + str(sys.getsizeof(arr)))
    if len(arr) <= 1:
        print("Memoria usada al final: " + str(sys.getsizeof(arr)))
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("Memoria usada durante:" + str(sys.getsizeof(arr)))
    return quick_sort(left) + middle + quick_sort(right)

nums10K=[]
nums100K=[]
nums1M=[]

for i in range(10001):
    nums10K.append(random.randint(1,1000))

for i in range(100001):
    nums100K.append(random.randint(1,10000))

for i in range(1000001):
    nums1M.append(random.randint(1,1000))

start_time=time.time()
bubble_sort(nums100K)
finish_time=time.time()
print("Tiempo: "+str(finish_time-start_time))

#Analisis de bubbleSort con 10k
#Memoria Usada:85176 bytes
#Tiempo: 44.62130904197693 segundos

#Analisis de bubbleSort con 100k
#Memoria Usada:800984 bytes
#Tiempo: +15 min

#Analisis de bubbleSort con 1M
#Memoria Usada:8448728 bytes
#Tiempo: Ni lo intente

#Analisis de QuickSort con 10K
#Memoria: 85176 bytes (inicio) 56 bytes (al final) 664 bytes (en medio)
#Tiempo: 0.01s

#Analisis de QuickSort con 100K
#Memoria: 800984 bytes (inicio) 56 bytes (al final) 26040 bytes (en medio)
#Tiempo: 0.1s

#Analisis de QuickSort con 1M
#Memoria: 8448728 bytes (inicio) 56 bytes (al final) 16184 bytes (en medio)
#Tiempo: 0.967s

#Analisis de MergeSort con 10K
#Memoria:Inicio:85176  Medio:128  Fin:85176
#Tiempo:0.01s

#Analisis de MergeSort con 100K
#Memoria:Inicio:72 Medio:80 Fin:800984
#Tiempo:0.23s

#Analisis de MergeSort con 1M
#Memoria:Inicio:88 Medio:72 Fin:8448728
#Tiempo:8.622s

