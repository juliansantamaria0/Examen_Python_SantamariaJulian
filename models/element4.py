class Element4:
    def __init__(self, nombre4, especialidad4,):
        self.nombre4 = nombre4
        self.especialidad4 = especialidad4

    def to_dict(self):
        return {
            "nombre4": self.nombre4,
            "especialidad4": self.especialidad4
        }