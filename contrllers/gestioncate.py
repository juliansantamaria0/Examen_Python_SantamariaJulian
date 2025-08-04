from utils.helpers import validate_input
from models.element2 import Element2

def add_element2(collection):
    nombre2 = validate_input("nombre2 de la categoria: ","el nombre2 no puede estar vacio.")
    descripcion2 = validate_input("descripcion2 de la categoria: ", "la descripcion2 no puede estar vacio.")

    element = Element2(nombre2, descripcion2,)
    collection.append(element)

    print("el elemento ha sido añadido a la coleccion")