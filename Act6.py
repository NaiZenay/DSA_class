import sys
numsList=range(1000001)
numsDiccionario={}
numsSet=set(numsList)

for i in range(1000001):
    numsDiccionario[i]=numsList[i]


#Lista de 1M de elementos
print(list(numsList))
#Diccionario de 1M de elementos
print(numsDiccionario)
#Set de 1M elementos
print(numsSet)

#Tamaño de memoria de la lista
print(sys.getsizeof(numsList))
#Tamaño de memoria de un diccionario
print(sys.getsizeof(numsDiccionario))
#Tamaño de memoria de un set
print(sys.getsizeof(numsSet))
