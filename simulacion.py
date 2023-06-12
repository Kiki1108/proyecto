from enfermedad import Enfermedad
from comunidad import Comunidad
from personas import Persona

class Simulacion():
    def __init__(self, dias, comunidad, enfermedad):
        self.__dias = dias
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad
        