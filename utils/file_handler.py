import json 
from models.element import Element

def load_collection(filename='data/ingredientes.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Element(**item) for item in data]
    except FileNotFoundError:
        print("no se encontro el archivo ingredientes.json se creara uno nuevo al guardar.")
        return []
    except json.JSONDecodeError:
        print("error al leer el archivo. El archivo puede estar corrupto o vacio.")
        return []

def save_collection(collection, filename='data/ingredientes.json'):
    try:
        with open(filename, 'w') as file:
            json.dump([elem.to_dict() for elem in collection], file, indent=4)
        print("ingredientes guardada correctamente.")
    except Exception as e:
        print(f"Error al guardar la colección: {e}")
