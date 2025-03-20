#Tabla Hash basica
class TablaHash:
    def __init__(self,length):
        self.length=length
        self.tabla=[[None]*length]

    def hash(self,key):
        hash_value=0
        for char in s:
            hash_value = (hash_value * 31) + ord(char)
        return hash_value%self.length

    def insert(self,key,value):
        index=self.hash(key)
        self.tabla[index]=[key,value]

    def


