import os
from ui.menu import show_menu
from utils.file_handler import load_collection, save_collection
from utils.file_handler2 import load_collection2, save_collection2
from utils.file_handler3 import load_collection3, save_collection3
from utils.file_handler4 import  load_collection4, save_collection4
from contrllers.gestioncate import add_element2
from contrllers.gestionIngre import add_element 
from contrllers.gestionhambur import add_element3
from contrllers.gestionchef import add_element4
from contrllers.HistorialIngre import sort_collection
from contrllers.historial import view_by_category

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona Enter para continuar...")

def main():
    collection = load_collection()

    while True:
        limpiar_pantalla()
        show_menu()
        opcion = input("seleccione una opcion: ")

        if not opcion.isdigit():
            print("por favor ingrese un numero valido. ")
            pausar()
            continue

        opcion = int(opcion)

        if opcion == 1:
            limpiar_pantalla()
            add_element(collection)
            save_collection(collection)
            pausar()

        elif opcion == 2:
            limpiar_pantalla()
            sort_collection(collection)
            pausar()

        elif opcion == 3:
            limpiar_pantalla()
            view_by_category(collection)
            pausar()

        elif opcion == 4:
            limpiar_pantalla()
            add_element2(collection)
            save_collection2(collection)
            pausar()


        elif opcion == 5:
            limpiar_pantalla()
            add_element3(collection)
            save_collection3(collection)
            pausar()

        elif opcion == 6:
            limpiar_pantalla()
            add_element4(collection)
            save_collection4(collection)
            pausar()

        elif opcion == 7:
            limpiar_pantalla()
            print("Gracias..... ¡Hasta luego!")
            break
        else:
            print("opcion invalida intentelo de nuevo")
            pausar()

if __name__ == "__main__":
    main()



