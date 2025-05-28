# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###

# Definición
"""resolver una logica concreta que intruduzcamos y 
 nos hace evitar errores porque la solucion a ese problema siempre en ese codigo
 y de alguna manera estara centralizada esa solucion y ya solo la tendremos que 
 mandar llamar, def es la palabra reservada para functions
 def nombre_function(): y todo lo tab despues de esto sera la funcion"""

def my_function():
    print("Esto es una función")


my_function() 
my_function()
my_function()
"""si ejecutamos no estariamos mirando el print dentro de def sino que se queda esperando
a ser llamada y ahora con my_fuction() ya se ejecuta eso que es la funcion en nuestro caso
es print("Esto es una funcion"), por lo que ya no necesitamos mas codigo para agregar de nuevo
ese print solo necesitamos llamar de nuevo la def

Con esto nos ahorramos codigo para cosas mas complejas y nos previene errores al intentar copiar
todo el codigo si no tuvieramos def"""
 

# Función con parámetros de entrada/argumentos dados al nombre de la funcion
print("funcion con parametros de entrada en la funcion")
"no se limita solo a desencadenar codigo,"
" tambien puede devolver y recibir codigo"


def sum_two_values(first_value, second_value): 
    print(first_value + second_value)
"""esta funcion es distitna a la anterior porque aqui el fist y secund value que estan
dentro de los () nos pide que le demos dos valores de entrada, por eso es un parametro 
de entrada y ademas estamos diciendo que se imprima la suma de ambos valores

Por lo que aqui lineas despues estamos dando esa entrada de paramentros a la def"""

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7") #57 porque concatana las dos cadenas de texto, xloq tipa es dinamico
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos dados al nombre de la funcion  y retorno de argumentos
print("funcion con parametros de entrada en la funcion y retorno")
"""basicamente retornar se ignifica que te va a entregar algo 
y a ese resultado lo tengo que guardar en una variable para poder 
mostrarlo de nuevo"""
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum
"""en este caso la variable en la que quiero que se guarde el resultado de 
la def es my_sum y le pido que me entrege osea que me retorne my_sum
pero seria lo mismo si solo pusiera return first_value + secund_value"""

#my_result = sum_two_values(1.4, 5.2) #retorna none porque sum_two_values es una def sin retorno
#print(my_result)

my_result = sum_two_values_with_return(10, 5) #resulado de la def la asignas a una variable
print(my_result) #y esta si retorna algo porque sum_two_value_with_return es una def de retorno
"""y al darle parametros como 10, 5 eso tambien lo agrego a otra variable"""

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")

# Función con parámetros de entrada/argumentos por defecto
"""dentro de def podemos dalrle un valor por defecto para que si no se agrega se muestre ese
valor, en este caso alias ="sin alias" pero como si tenemos alias que es MoureDev
nos da el parametro correcto"""

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("Brais", "Moure") #sin valor de alias
print_name_with_default("Brais", "Moure", "MoureDev") #con valor de alias "MoureDev" 

# Función con parámetros de entrada/argumentos arbitrarios y dinamicos
"""con * en los paramentros le pedimos que le podemos pasar cualquiera"""

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")
