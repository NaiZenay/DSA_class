import csv
import time

#Clase basica para almacenar la informacion de los registros
class Producto():
    def __init__(self, nombre, descripcion, ficha_tecnica, bloque, certificado, destacado, tapizado, categoriaId,
                 disenadorId):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ficha_tecnica = ficha_tecnica
        self.bloque = bloque
        self.certificado = certificado
        self.destacado = destacado
        self.tapizado = tapizado
        self.categoriaId = categoriaId
        self.disenadorId = disenadorId

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Descripcion: {self.descripcion}\n"
                f"Ficha Tecnica: {self.ficha_tecnica}\n"
                f"Bloque: {self.bloque}\n"
                f"Certificado: {self.certificado}\n"
                f"Destacado: {self.destacado}\n"
                f"Tapizado: {self.tapizado}\n"
                f"CategoriaId: {self.categoriaId}\n"
                f"DisenadorId: {self.disenadorId}")

#Mi implementacion de la tarea 9
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

# Forma facil con la libreria de csv
registros = []
with open('productos.csv', encoding="utf-8") as productos:
    productos_dict = csv.DictReader(productos, delimiter="#")
    for row in productos_dict:
        registros.append(row)

print("================================================================")

#A manita
with open('productos.csv', encoding="utf-8", newline='') as productospt2:
    # Genera la lista de campos que tendra el diccionario
    #campos = [campo.strip('\"') for campo in productospt2.readline().strip("\n").split("#")]   ----> al final no use esto pero era para hacer un zip con los datos
    registros_csv = productospt2.readlines()

    dictProductos = {}
    tabla_productos = TablaHash(len(registros_csv))

    # Lee cada registro del archivo lo limpia de cosas incesarias y guarda una lista de los datos en una lista nueva
    lista_registros = []
    for i in range(1, len(registros_csv)):
        campos_X_registro = []
        for columna in registros_csv[i].strip("\n").split("#"):
            campos_X_registro.append(columna.strip('\"'))
        lista_registros.append(campos_X_registro)

    for i in range(len(lista_registros)):
        #mapeo de producto en un Obj
        prod = Producto(lista_registros[i][1], lista_registros[i][2], lista_registros[i][3], lista_registros[i][4],
                        lista_registros[i][5], lista_registros[i][6], lista_registros[i][7], lista_registros[i][8],
                        lista_registros[i][9])
        # Toma el id como clave
        dictProductos[lista_registros[i][0]] = prod
        tabla_productos.insert(lista_registros[i][0],prod)

    #Impresion de datos con diccionario de python
    #for k, v in dictProductos.items():
    #    print("Clave:" + k)
    #    print(v)

    #Impresion de datos con mi tabla
    #print(tabla_productos)

    #Pruebas de tiempo
    start=time.time()

    #Con mi tabla
    print(str(tabla_productos.get("51748b4c-5138-464e-bc11-920c01caeb70")))

    #Con diccionario de Python
    print(dictProductos["51748b4c-5138-464e-bc11-920c01caeb70"])

    finish=time.time()

    print("Tiempo de consulta:"+str(finish-start))