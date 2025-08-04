def view_by_category(collection):
    print("¿Que categoria deseas ver?")
    print("1. Ver por nombre")
    print("2. Ver por descripcion")
    print("3. Ver por stock")
    print("4. Ver por precio")
    print("5. Regresar al Menu Principal")
    opcion = input("Selecciona una opcion (1-5): ")

    if opcion == '1':
        print("nombre:")
        found = False
        for elem in collection:
            if elem.nombre.lower() == 'nombre':
                print(f"- {elem.nombre}")
                found = True
        if not found:
            print("No hay nombres en la coleccion.")
    elif opcion == '2':
        print("descripciones en la coleccion:")
        found = False
        for elem in collection:
            if elem.descripcion.lower() == 'descripcion':
                print(f"- {elem.descripcion})")
                found = True
        if not found:
            print("No hay descripciones en la colección.")
    elif opcion == '3':
        print("stock en la colección:")
        found = False
        for elem in collection:
            if elem.stock.lower() == 'stock':
                print(f"- {elem.stock} )")
                found = True
        if not found:
            print("No hay stock en la coleccion.")
    elif opcion == '4':
        print("precios en la colección:")
        found = False
        for elem in collection:
            if elem.precio.lower() == 'precio':
                print(f"- {elem.precio} )")
                found = True
        if not found:
            print("No hay precios en la coleccion.")
    elif opcion == '4':
        return
    else:
        print("Opcion invalida. Regresando al menu principal.")