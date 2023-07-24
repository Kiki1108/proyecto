import random

class Vacuna():
    def __init__(self, restante, inmunidad):
        """
        Inicializa los valores de la clase Vacuna

        Atributos:
            inicio[int]: Día en que se empieza a entregar la vacuna
            total [int]: Total de personas
            tasa [int]: porcentaje de personas que pueden recivir la vacuna
            inmunidades [ALGO?]: Algo???
            vacunas_restantes [list]: Cantidad de vacunas que hay por tipo
        """
        self.__inmunidad = inmunidad
        self.__vacunas_restantes = restante


    def get_vacunas_restantes(self):
        return self.__vacunas_restantes


    def is_inmune(self):
        if random.randint(0, 100) <= self.__inmunidad:
            return True
        return False


    def gastar_vacunas(self, a):
        self.__vacunas_restantes = self.__vacunas_restantes - a
