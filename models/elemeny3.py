class Element3:
    def __init__(self, nombre3 ,categoria3 ,ingredientes3, precio3, chef3):
        self.nombre3 = nombre3
        self.categoria3 = categoria3
        self.ingredientes3 = ingredientes3
        self.precio3 = precio3
        self.chef3 = chef3

    def to_dict(self):
        return {
            "nombre3": self.nombre3,
            "categoria3": self.categoria3,
            "ingredientes3": self.ingredientes3,
            "precio3": self.precio3,
            "chef3": self.chef3
        }