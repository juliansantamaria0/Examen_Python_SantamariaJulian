import json 
from models.elemeny3 import Element3

def load_collection3(filename='data/hamburguesas.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Element3(**item) for item in data]
    except FileNotFoundError:
        print("no se encontro el archivo hamburguesas.json se creara uno nuevo al guardar.")
        return []
    except json.JSONDecodeError:
        print("error al leer el archivo. El archivo puede estar corrupto o vacio.")
        return []

def save_collection3(collection, filename='data/hamburguesas.json'):
    try:
        with open(filename, 'w') as file:
            json.dump([elem.to_dict() for elem in collection], file, indent=4)
        print("hamburguesas guardada correctamente.")
    except Exception as e:
        print(f"Error al guardar la colección: {e}")