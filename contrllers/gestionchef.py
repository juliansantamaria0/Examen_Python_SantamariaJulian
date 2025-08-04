from utils.helpers import validate_input
from models.element4 import Element4

def add_element4(collection):
    nombre4 = validate_input("nombre del chef: ","el nombre del chef no puede estar vacio.")
    especialidad4 = validate_input("especialidad del chef: ", "la especialidad del chef no puede estar vacio.")

    element = Element4(nombre4, especialidad4,)
    collection.append(element)

    print("el elemento ha sido añadido a la coleccion")