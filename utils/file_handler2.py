import json 
from models.element2 import Element2

def load_collection2(filename='data/categorias.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Element2(**item) for item in data]
    except FileNotFoundError:
        print("no se encontro el archivo categorias.json se creara uno nuevo al guardar.")
        return []
    except json.JSONDecodeError:
        print("error al leer el archivo. El archivo puede estar corrupto o vacio.")
        return []

def save_collection2(collection, filename='data/categorias.json'):
    try:
        with open(filename, 'w') as file:
            json.dump([elem.to_dict() for elem in collection], file, indent=4)
        print("categorias guardada correctamente.")
    except Exception as e:
        print(f"Error al guardar la colección: {e}")