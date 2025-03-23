#Tabla Hash basica
class TablaHash:
    def __init__(self,length):
        self.length=length
        self.tabla=[LinkedList() for _ in range(length)] #Crea una lista ligada en cada espacio de la tabla hash


    #Funcion hash sacada de internet
    def hash(self,key):
        hash_value=0
        for char in key:
            hash_value = (hash_value * 31) + ord(char)
        return hash_value%self.length

    def insert(self,key,value):
        index=self.hash(key)
        #Entra a la tabla y a la lista ligada de ese indice
        key_value=(key,value)
        self.tabla[index].insert(key_value)


    #Obtiene solo el indice del espacio de la lista ligada
    def get(self,key):
        index=self.hash(key)
        return self.tabla[index].get(key) # accede a la lista ligada del inidice generado

    def __str__(self):
        result=""
        for data in self.tabla:
            result += data.__str__()
        return result


#implementacion basica de una lista ligada
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0

    def insert(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=Node(value)

        self.length+=1

    def get(self,value):
        current=self.head
        while current is not None:
            if current.value[0]==value: #Accede a la llave de la tupla guardada en el nodo
                return current.value
        return None

    def __str__(self):
        result="["
        current=self.head
        while current is not None:
            result += str(current.value)
            current=current.next
        result += "]"
        return result



#puntaje de equipos
puntaje=TablaHash(5)

puntaje.insert("Ian",3)
puntaje.insert("Brayan",5)
puntaje.insert("Angel",5)
puntaje.insert("Cris",5)
puntaje.insert("Julia",5)
puntaje.insert("Angela",5)
puntaje.insert("Cristal",5)


print(puntaje)