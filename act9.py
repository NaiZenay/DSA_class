#Tabla Hash basica
from os import remove


class TablaHash:
    def __init__(self,length):
        self.length=length
        self.tabla=[None for _ in range(length)]
        self.dummy_var="80085"

    #Funcion hash sacada de internet
    def hash(self,key):
        hash_value=0
        for char in key:
            hash_value = (hash_value * 31) + ord(char)
        return hash_value%self.length

    def insert(self,key,value):
        original_index=self.hash(key) #Guarda el indicie original para evitar loop infinito
        index = self.hash(key)
    #Mientras el inidice no este vacio       y    no se la bandera de info borrada
        while self.tabla[index] is not None and self.tabla[index] is not self.dummy_var:
            index = (index + 1) % self.length #Linear probbing (busca espacion libres)
            #Comprueba que la tabla aun tenga espacio libre si ya dio la vuelta ahi muere
            if index == original_index:
                print("Tabla llena")
                return
        self.tabla[index]=(key,value)

    def get(self,key):
        index=self.hash(key)
        original_index=self.hash(key)
        while self.tabla[index] is not None and self.tabla[index] is not self.dummy_var:
            if self.tabla[index] is not None and self.tabla[index][0] == key:
                return self.tabla[index]
            index = (index + 1) % self.length
            if index == original_index:
                break
        return None

    def remove(self,key):
        original_index=self.hash(key)
        index=self.hash(key)
        while self.tabla[index] is not None and self.tabla[index] is not self.dummy_var:
            if self.tabla[index][0] == key:
                self.tabla[index] = self.dummy_var
                break
            index = (index + 1) % self.length
            if index == original_index:
                break
        return


    def __str__(self):
        result=""
        for data in self.tabla:
            if data is not None and type(data) is tuple:
                result += "("
                result += str(data[0])+","+str(data[1])
                result += ")"
            else:
                result += "("+str(data)+")"
        return result

#puntaje de equipos (Factor de carga 0.5)
puntaje=TablaHash(10)

puntaje.insert("Ian",3)
puntaje.insert("Brayan",5)
puntaje.insert("Angel",3)
puntaje.insert("Cris",2)
puntaje.insert("aae",10)#Clave para forzar colision

print(puntaje)

puntaje.remove("Ian")

print(puntaje)

#Tabala con Factor de carga 0.7
puntaje2=TablaHash(10)
for i in range(1,8):
    puntaje2.insert("equipo{}".format(i),i)

print(puntaje2)


#Tabla con Factor de carga 0.9
puntaja3=TablaHash(10)
for i in range(1,10):
    puntaja3.insert("team{}".format(i),i)

print(puntaja3)

#Resultados de la consola
#Tabla 1
#(Ian,3)(Cris,2)(None)(None)(None)(Brayan,5)(aae,10)(Angel,3)(None)(None)
#Tabla 1 despues de borrar un elemento
#(80085)(Cris,2)(None)(None)(None)(Brayan,5)(aae,10)(Angel,3)(None)(None)
#Tabla 2
#(equipo3,3)(equipo4,4)(equipo5,5)(equipo6,6)(equipo7,7)(None)(None)(None)(equipo1,1)(equipo2,2)
#tabla3
#(team9,9)(None)(team1,1)(team2,2)(team3,3)(team4,4)(team5,5)(team6,6)(team7,7)(team8,8)
