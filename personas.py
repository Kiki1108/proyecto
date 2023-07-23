class Persona():
    def __init__(self, id, nombre):
        """
        Inicializa los valores de la clase Persona
        
        Atributos:
            id [int]: Identificador único de la persona
            nombre [list]: Nombre asignado de una persona (un nombre y dos apellidos)
            enfermedad [Enfermedad]: Enfermedad que tendra la persona
            estado [str]: Indica el estado de salud de la persona ("S":suceptible, "E":enfermo, "I":Inmune, "M":Muerto)
            contador [int]: Contador de días que dura la enfermedad en la persona
        """
        self.__id = id
        self.__nombre = nombre
        self.__estado = "S"
        self.__contador = None


    def get_id(self):
        return self.__id


    def get_nombre(self):
        return self.__nombre


    def get_estado(self):
        return self.__estado


    def get_contador(self):
        return self.__contador


    def set_estado(self, estado):
        if estado in ["S", "E", "I", "M", "V"]:
            self.__estado = estado


    def set_contador(self, contador):
        self.__contador = contador


    def restar_contador(self):
        """
        Resta la cantidad de dias que deberia durar la enfermedad en la persona
        """
        self.__contador = self.__contador -1
