#Tabla Hash basica
class TablaHash:
    def __init__(self,length):
        self.length=length
        self.tabla=[LinkedList]*length #Crea una lista ligada en cada espacio de la tabla hash


    #Funcion hash sacada de internet
    def hash(self,key):
        hash_value=0
        for char in key:
            hash_value = (hash_value * 31) + ord(char)
        return hash_value%self.length

    def insert(self,key,value):
        index=self.hash(key)
        self.tabla[index].insert(key,value)# accede a la lista ligada del inidice generado

    def get(self,key):
        index=self.hash(key)
        for k,value in self.tabla:
            if k == key:
                return value
            return None

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
        if self.head==None:
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
            if current.value==value:
                return current
        return None

    def get_length(self):
        return self.length


#puntaje de equipos
equipos=TablaHash(5)


