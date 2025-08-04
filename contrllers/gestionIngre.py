from utils.helpers import validate_input
from models.element import Element

def add_element(collection):
    nombre = validate_input("nombre del ingrediente: ","el nombre del ingrediente no puede estar vacio.")
    descripcion = validate_input("descripcion del ingrediente: ", "la descripcion del ingrediente no puede estar vacio.")
    stock = validate_input("stock del ingrediente: ", "El stock del ingrediente no puede estar vacio.")
    precio = input("precio del ingrediente: ").strip()

    element = Element(nombre, descripcion, stock, precio)
    collection.append(element)

    print("el elemento ha sido añadido a la coleccion")

