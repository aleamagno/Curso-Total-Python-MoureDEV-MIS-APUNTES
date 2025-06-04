# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###
"""es otra forma de agrupar codigo, dividir, dotar de funcionalidad"""
# Definición
"""nos sirve para dotar de inicio y fin un objeto 
Es como decirle que todo lo que este dentro de una clase tiene que responder a una
cierta logica, por ejemplo si tenemos una clase persona pues que todo dentro sea justamente
relacionado con persona; Es darle identidad al codigo dentro de un ambito de aplicacion"""

class MyEmptyPerson: #en camelkeys
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson) #llamar la clase sin () o con ellos
print(MyEmptyPerson()) #seran necesarios () cuando tengan algo que necesite ejecutarse

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública fuera de class person se puede modificar
        self.__name = name  # Propiedad privada con __ para que desde fuera de class person no se pueda modificar

    def get_name (self):
        return self.__name
        #la prop privada no la va a leer desde fuera por lo que tenemos que traerla con def return

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure") #aqui le doy valores a las propiedades de la clase person
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)
"""en el primer ejemplo pusimos Brais como nombre y Moure como surname, en este segundo"
 "ejemplo ponemos primero como name Brais, Surname Moure y alias Mouredev y lo imprime
 perfecto, 
 pero ademas modemos modificar el fullname de la clase person en estr caso a Hector de Leon
 (el loco de los perros) y fijate que () porque la propiedad fullname tiene que alias puede
 ser () y asi lo lee y la imprimimos luego y se imprime con los cambios de ahora"""

my_other_person.full_name = 666
print(my_other_person.full_name)
"""def init self es un contructor de clase donde le asignamos ciertos valores o propiedades 
 a nuestra clase; 
 seguido de eso tenemos que nombar self.nombre de variable= para definir una variable a ejecutar
 siempre es self porque es literal traduccion tu mismo que hace referencia a algo dentro
 de las propiedades de esa clase"""