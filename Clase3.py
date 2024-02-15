
def opcion_a_suma


def main():
    
    while True :
        print("Opciones:")
        print("1. Realizar acción A (Suma)")
        print("2. Realizar acción B (Producto)")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        

        if opcion == '1':
            opcion_a_suma()
        elif opcion == '2':
            opcion_b_producto()
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
       





if __name__ == "__main__":
    main()