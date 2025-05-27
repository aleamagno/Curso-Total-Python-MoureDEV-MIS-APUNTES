# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

my_set = set() #llamando a set()
my_other_set = {} #con {}

print(type(my_set))
print(type(my_other_set))  # set vacio Inicialmente es un diccionario porque ambos son con{}

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada como las litas

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Moure" in my_other_set)
print("Mouri" in my_other_set)

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear() #clear es deja vacio 
print(len(my_other_set))

del my_other_set #del lo elimina directamente el objeto por completo
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])
"""es un poco arriesgado porque como set es sin orden y al crear una lista e
intentar imprimir el elemento 0 nos puede dar otro que no es el que desamos"""

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
"""set no admite repetidos y al agregar de nuevo otra vez el set por eso no me lo agrega sino
hasta que ese union si tiene otros valores nuevos"""

print(my_new_set.difference(my_set))
"""esta diferencia es solo entre my_set y my_new_set sin el union java,c# porque este
union lo he hecho solo para el print y no se ha almacenado en una varibale nueva"""
