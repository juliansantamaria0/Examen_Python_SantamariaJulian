class Element2:
    def __init__(self, nombre2, descrpcion2,):
        self.nombre2 = nombre2
        self.descrpcion2 = descrpcion2

    def to_dict(self):
        return {
            "nombre2": self.nombre2,
            "descrpcion2": self.descrpcion2
        }