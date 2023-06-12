import json

from enfermedad import Enfermedad

with open("nombres_apellidos.json") as archivo:
    dic = json.loads(archivo)

class Comunidad():
    def __init__(self, poblacion, enfermedad) -> None:
        self.__poblacion = poblacion
        self.__enfermedad = enfermedad




        