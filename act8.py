#Diccionario con puntajes de equipo de fut bol
equipos={
    "chivas":3,
    "atlas": 8,
    "america": 2,
    "barcelona": 1,
    "Real M": 0,
    "Pumas": 0,
    "San luis": 4,
    "Santos": 6,
    "Atletico M": 1,
    "Francia": 3,
}

# Una tabla hash toma la clave asiganda al valor
# y la procesa por medio de la funcion Hash para obtener
# el indice en la lista de la tabla hash de volver el valor

print(equipos["chivas"]) #Acceso individual a cada dato con la clave

for equipo,puntaje in equipos.items(): #Devuelve una tupla con las claves y valores
    print(f"Puntaje de {equipo} : {puntaje}")

#Ventaja
#Acceso a los valores en tiempo contaste

#Desvetajas (mi opinion)
#Manjear las colisiones, nada te asegura no tenerlas y al manejarlas pierda la ventaja
#Necesitas conocer la clave (ni tan desventajoso pq para eso es)


