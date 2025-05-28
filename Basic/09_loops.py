# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### Loops ###
"""es un mecanismo que nos sirve para iterar
que es iterar? es intentar repetir algo
es basicamente pasar por el mismo codigo varias veces con un solo codigo"""


# While
"""while usa condiciones, MIENTRAS SEA VERDADERO HAS ALGO"""

my_condition = 0

while my_condition < 10:
    print(my_condition)
    """ la condicion = 0 y si mi conficion = 0 entonces imprime condicion
    y la vuelve a tomar y como de nuevo es cero la imprime de nuevo y asi 
    hasta el infinito, ES COMO UNA SERPIENTE QUE SE COME A SI MISMA"""
    my_condition += 2 
    """para que no este al infinito le agregamos algo a 
    la condicion entonces tiene que parar hasta que la condicion de while se 
    cumpla cada impresion seria en una linea separada"""
else:  # Es opcional else pero puede servir para informar que el bucle ha finalizado
    print("Mi condición es mayor o igual que 10")
"""este else pertenece al while pero podria funcionar igual con if porque 
despues de while leeria el if, no acepta elif"""
print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15, Se detiene la ejecución")
        break #brake es para que pare el bucle 
    print(my_condition)

print("La ejecución continúa")

# For
"""nos sirve para iterar un listado de elementos"""
print("inicia for list que guardan elementos una a uno")
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)
"""mientras que while hace que el codigo se repita infinitas veces en funcion de una condicion, 
for hace que se repita tantas veces como elementos que tengamos iterables por lo que es finita 
y cada vez que le de una vuelta a for va a estar accediendo a uno de esos elementos del listado"""

print("inicia for tuple guardan elementos pero no se pueden modificar")
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

print("inicia for set, guardan elementos que no esten repetidos")
for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

print("inicia for dict, guardan elementos clave -> valor pero con for solo muestra el keys "
"y si queremos ver los vlaores entonces convertiriamos el dict a list y quedaria como"
"for element in list(my_dict.values()): ó solo my_dict.values(): porque en si values es "
"capaz de traerlos en formato lista ")
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue #es lo contrario a brake y muestra 1 en este caso, no tiene tanto sentido 
    print("Se ejecuta continue")
else:
    print("El bluce for para diccionario ha finalizado")
"""continue es es vuelva a for sin ver lo que esta debajo
break es termina todo el bucle"""