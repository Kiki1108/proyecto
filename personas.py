

class Persona():
    def __init__(self, id, nombre, enfermedad, estado):
        self.__id = id                  # int, identificador único de la persona
        self.__nombre = nombre          # [nombre, apellido, apellido]    
        self.__enfermedad = enfermedad  # class enfermedad
        self.__estado = "S"             # str ("S":suceptible, "E":enfermo, "I":Inmune, "M":Muerto)


    def get_id(self):
        return self.__id
    

    def get_nombre(self):
        return self.__nombre
    

    def get_estado(self):
        return self.__estado
    

    def set_estado(self, estado):
        if estado in ["S", "E", "I", "M"]:
            self.__estado = estado
