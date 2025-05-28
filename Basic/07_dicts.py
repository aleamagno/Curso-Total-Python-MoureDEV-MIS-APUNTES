# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}
"""la diferencia entre los sets es que aqui tenemos una relacion-clave_valor
mi --´nombre´:-- funcionando como clave lo relaciono a otro valor ´brais´
esta es una buena estructura para relacionar datos"""

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}
print(my_dict["Edad"],"provando si puedo buscar por valor")
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Moure" in my_dict) #aunque este en apellido:Moure lo que busca es por clave por eso false
print("Apellido" in my_dict)
print(my_dict["Apellido"]) #de esta forma si nos da directamente Moure
      
# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización de clave de dict

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print("intento de actualizar key de un valor")
#my_dict["nuevo apellido"]=" Aurelio"
print(my_dict)
# Eliminación de un elemento del dict

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items()) #listado de cada uno de los items
print(my_dict.keys()) #solo un listado de las claves
print(my_dict.values()) #nos da los valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev") #mete el valor a todas las claves
print((my_new_dict))

my_values = my_new_dict.values() 
"""para tener un valor en lugar de clave crea una variable que contenga .values para que nos de los valores del diccionario porque 
basciamente es crear una lista de valores"""
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
