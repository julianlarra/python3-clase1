def mostrar_menu():
        print('#'*20  ) 
        print(  "\n Opciones:")
        print("1. Realizar acción A (Suma)")
        print("2. Realizar acción B (Producto)")
        print("0. Salir \n"  )
        print('/-'*10  )

def opcion_a_suma(num1,num2):
    suma = num1 + num2
    return suma

def opcion_b_producto(num1,num2):
     producto= num1 * num2
     return producto
    

def main():
    opcion= 3
    while opcion != 0 :

        mostrar_menu()

        opcion = int(input("\n Ingrese el número de la opción deseada: "))
  
        if opcion == 1:
            
              print(f'\n la suma de los numeros es: {opcion_a_suma(4,6)}')
        
        elif opcion == 2:
            print(f'\n El producto de los numeros es: {opcion_b_producto(3,5)}')
            
        elif opcion == 0:
            print("\n Saliendo del programa. ¡Hasta luego!")
            break
        else : 
             print('\n Elija una opcion valida.')

if __name__ == "__main__":
    main()