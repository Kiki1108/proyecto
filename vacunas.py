import random

class Vacunas():
    def __init__(self, inicio, total, tasa, inmunidades):
        self.__inicio = inicio
        self.__total = total
        self.__tasa = tasa
        self.__inmunidades = inmunidades
        self.__vacunas_restantes = [total * 25 / 100, total * 50 / 100, total * 25 / 100]


    def get_inicio(self):
        return self.__inicio
    

    def get_total(self):
        return self.__total
    

    def get_tasa(self):
        return self.__tasa
    

    def get_vacunas_restantes(self):
        return self.__vacunas_restantes
    

    def is_inmune(self, i):
        if random.randint(0, 100) <= self.__inmunidades[i]:
            return True
        return False


    def gastar_vacunas(self, a, b, c):
        self.__vacunas_restantes = [self.__vacunas_restantes[0] - a, self.__vacunas_restantes[1] - b, self.__vacunas_restantes[2] -c]
