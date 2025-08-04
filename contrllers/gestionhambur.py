from utils.helpers import validate_input
from models.element import Element

def add_element3(collection):
    nombre3 = validate_input("nombre de la hamburguesa: ","el nombre de la hamburguesa no puede estar vacio.")
    categoria3 = validate_input("categoria de la hamburguesa: ", "la categoria de la hamburguesa no puede estar vacio.")
    ingredientes3 = validate_input("ingredientes de la hamburguesa: ", "los ingredientes de la hamburguesa no puede estar vacio.").strip
    precio3 = input("precio de la hamburguesa: ").strip()
    chef3 = validate_input("nombre de la hamburguesa: ","el nombre de la hamburguesa no puede estar vacio.") 

    element = Element(nombre3, categoria3, ingredientes3, precio3, chef3)
    collection.append(element)

    print("el elemento ha sido añadido a la coleccion")
