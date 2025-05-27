# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #para definir el tipo de formato
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #es la manera mas rapida y logica de usar el formateo

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)
"""basicamente python tiene 6 letras y la queremos descomponer o desempaquetar
entonces al agregar las variables del tamaño de python podemos impimir justamente
el caracter que deseamos, para esto seriviria el desempaquetado"""


# División

language_slice = language[1:3]
print(language_slice)
"""nos muestra el indice de cada palabra sin contar la 3 que seria aqui yt de python"""

language_slice = language[1:]
print(language_slice)
"""quitando el final nos muestra desde la uno hasta terminar
el string y nos daria ython"""

language_slice = language[-2]
print(language_slice)
"""comenzaria de final a inicio siendo -1 la ultima letra y aqui el 
resultado es o"""

language_slice = language[0:6:2]
print(language_slice)
"""sacarlos por separado nos daria pto no tengo idea porque si
python
123456
entonces nos omite lo que le estamos diciendo es bastante rebuscado pero por si acaso
porque estamos agregando 3 valores a tomar entonces toma unos como rango y despues el otro rango etc"""

# Reverse

reversed_language = language[::-1]
print(reversed_language)
""" para imprimirlo al reves"""

# Funciones o Metodos del lenguaje

print(language.capitalize()) #pone letra capital mayus
print(language.upper()) #para poner mayuscula todas
print(language.count("t")) #cuenta las veces que aparece el valor
print(language.isnumeric()) #si es un numero
print("1".isnumeric())
print(language.lower()) #
print(language.lower().isupper()) #lower minusculas y isupper para comprobar si es mayus
print(language.startswith("Py")) #si empieza con py en este caso
print("Py" == "py")  # No es lo mismo porque es sensible a mayus y minus
#trabajo ahora desde pc work
