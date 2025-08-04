import json 
from models.element4 import Element4

def load_collection4(filename='data/chefs.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Element4(**item) for item in data]
    except FileNotFoundError:
        print("no se encontro el archivo chefs.json se creara uno nuevo al guardar.")
        return []
    except json.JSONDecodeError:
        print("error al leer el archivo. El archivo puede estar corrupto o vacio.")
        return []

def save_collection4(collection, filename='data/chefs.json'):
    try:
        with open(filename, 'w') as file:
            json.dump([elem.to_dict() for elem in collection], file, indent=4)
        print("chefs guardada correctamente.")
    except Exception as e:
        print(f"Error al guardar la colección: {e}")