def sort_collection(collection):
    print("Registro y almacenamiento de ingredientes utilizados.")
    print("1. por nombre")
    print("2. por descripcion")
    print("3. por stock")
    print("4. por precio")

    opcion = input("seleccione una opcion: ")

    if opcion == '1':
        collection.sort(key=lambda x: x.nombre.lower())
        print("ingredientes ordenada por nombre")
    elif opcion == '2':
        collection.sort(key=lambda x: x.descripcion.lower())
        print("ingredientes ordenada por descripcion")
    elif opcion == '3':
        collection.sort(key=lambda x: x.stock.lower())
        print("ingredientes ordenada por stock")
    elif opcion == '4':
        collection.sort(key=lambda x: x.precio.lower())
        print("ingredientes ordenada por precio")
    else:
        print("opcion invalida no se realizo ninguna ordenacion.")