'''2. Crear una lista con 5 elementos y luego aplica los siguientes
accionables:
↪ Imprimir el último elemento
↪ Modificar el valor del tercer elemento
↪ Agregar dos elementos
↪ Eliminar algún elemento
● Guardar en un archivo llamado ejercicio2.py'''


lista = ['lunes', 'martes', 'miercoles','jueve', 'viernes'] 
print(lista)
print(f'El ultimo elemento de la lista es : {lista[-1]}') 
lista[2]='MIERCOLES'
print(lista)
lista.append('sabado')
lista.append('domingo')
print(lista)
lista.pop(0)
print(lista)