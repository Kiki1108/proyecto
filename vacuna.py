import random

class Vacuna():
    def __init__(self, restante, inmunidad):
        """
        Inicializa los valores de la clase Vacuna

        Atributos:
            inmunidad [int]: Porcentaje de inmunidad de la vacuna
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
