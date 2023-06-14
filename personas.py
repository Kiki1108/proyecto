class Persona():
    def __init__(self, id, nombre, enfermedad, estado):
        # int, identificador único de la persona
        self.__id = id
        # [nombre, apellido, apellido]
        self.__nombre = nombre
        # class enfermedad
        self.__enfermedad = enfermedad
        # str ("S":suceptible, "E":enfermo, "I":Inmune, "M":Muerto)
        self.__estado = "S"


    def get_id(self):
        return self.__id


    def get_nombre(self):
        return self.__nombre


    def get_estado(self):
        return self.__estado


    def set_estado(self, estado):
        if estado in ["S", "E", "I", "M"]:
            self.__estado = estado
