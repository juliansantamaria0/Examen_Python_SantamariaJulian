class Element:
    def __init__(self, nombre, descrpcion, stock, precio=None):
        self.nombre = nombre
        self.descrpcion = descrpcion
        self.stock = stock
        self.precio = precio

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "descrpcion": self.descrpcion,
            "stock": self.stock,
            "precio": self.precio
        }
    