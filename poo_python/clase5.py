'''2. Crear una clase llamada Animal, otra llamada Perro y otra llamada
Águila.
↪ La clase Animal tiene:
○ atributo cantidad_patas: numérico
○ atributo tipo: vertebrado/invertebrado
○ método comer(): retorna un string “estoy comiendo”
↪ La clase Perro hereda de Animal y agrega:
○ atributo nombre: texto
○ atributo raza: texto
○ método correr(): retorna un string “estoy corriendo”
↪ La clase Aguila hereda de Animal y agrega:
○ método volar(): retorna un string “estoy volando”
● Guardarlo en un archivo llamado ejercicio2.py'''

class Animal:
    def __init__(self, cantidad_patas, tipo) :
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "estoy comiendo"
    
class Perro:
    def __init__(self, cantidad_patas, tipo, nombre, raza) :
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza =raza
    
    def correr(self):
        return "estoy corriendo"
    
class Aguila: 
    def __init__(self, cantidad_patas, tipo) :
        super(). __init__( cantidad_patas, tipo)

    def volar(self):
        return "estoy volando"
    

perro1 = Perro(4,"Vertebrado", "Fito", "Colie")

print(perro1.raza)