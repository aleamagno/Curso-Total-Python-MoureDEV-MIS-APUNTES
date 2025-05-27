# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ###

# Definición

my_tuple = tuple() #agregas tupla llamando tuple
my_other_tuple = () #agreas tupla con ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Brais"))
print(my_tuple.index("Moure")) #index es para darnos el indice de el valor designado
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment
#AGREGAR, ELIMINAR, ETC ETC NO EXISTE EN TUPLAS POR ESO SON VALORES CONSTANTES

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas
"""TUPLAS son inmutables pero por si necesitamos algunos elementos especificos
podemos hacer una subtupla seleccionando solo esos elementos"""
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista para hacerla mutable y poder editar los valores orignales

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
