# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición
"""una lista es una estructura de datos
la diferencia con list y tuplas es que a una variable si quires
que sea de tipado dinamico lista coloca list(aqui dentro lo que quieras)
igual para las tuplas coloca tuple()
otra forma mas rebuscada de ver es lista [] y tupla() y eso puede
hacerte confundir, 
si quieres que sea de tipo fijo colocas variable_list=() entre comillas
para que sea justa la lista
las tuplas son parecidas a list solo que inmutables"""
my_list = list() #list() es una lista tipado dinamico, la tomaria como lista por list siempre comienza con 0 el primer elemento
my_other_list = [] 
list_tipo_fijo=(100,200,300) #variable=()es una lista de tipado fijo,  seria clase tupla por ()
list_tipo_fijo2=[400,500,600] #seria clase list
print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"] #la lista puede ser de distintos tipos de datos

print(type(my_list))
print(type(my_other_list))
print(type(list_tipo_fijo))
print(type(list_tipo_fijo2))

# Acceso a elementos y búsqueda dentro de la lista nombrando el indice del elemento

print(my_other_list[0]) #el primer elemento de la lista
print(my_other_list[1]) #el segundo elemento de la lista
print(my_other_list[-1]) #el ultimo elemento de la lista
print(my_other_list[-4]) #es llegar de nuevo al inicio con nuestra lista de 4 elementos
# print(my_other_list[4]) IndexError porque elemento 4 no existe
# print(my_other_list[-5]) IndexError porque elemento -5 no existe 
print(my_list.count(30)) #.count es para ver cuantas veces se repite

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list #desigando variables a mi lista con coma, tiene que tener todos los elementos de la lista
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) #esta es otra forma pero mas rebuscada para designar valores de mi lista a varaibles

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list) 

# Creación, inserción, actualización y eliminación ESTO NO LO TINEN LAS TUPLAS POR ESO DE QUE LAS TUPLAS SON FIJAS

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Rojo") #inserta un valor en indice especificado
print(my_other_list)

my_other_list[1] = "Azul" #cambia el valor del indice designado
print(my_other_list)

my_other_list.remove("Azul") #elimina valor mencioado
print(my_other_list)

my_list.remove(30) #elimina el primer valor mencionado
print(my_list)

print(my_list.pop()) #.pop no muestra el ultimo valor 
print(my_list)
print(my_list.pop(2)) 
print("mi pop element")#lo que hace es que nos muestra ese valor que omitio antes
                        
print(my_list)
my_pop_element = my_list.pop(2) ##guardar elemento pop creamos en otra variable, asi desapilamos un valor de una lista
print(my_pop_element)
print(my_list) #me da 52 porque 2 es el nuevo elemento de my list 35,24,52,30
print("debeira mostrar mi lista sin el valor de pop")
del my_list[2] #elimina por indice el valor designado
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)
"""que interesante el .copy porque podria resolver el que las variables
no sean fijas, si tengo una variable originalque voy a modificar ahora 
pero la original la voy a seguir usando despues entonces a variable origial 
le hago un .copy para tomarla despues de nuevo y asi no se modifica con la modificacion 
que haga ahora"""

my_new_list.reverse() #valores ordenados al reves, primero llamas .reverse y luego lo imprimes
print(my_new_list)

my_new_list.sort() #sort para ordenar 
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))
