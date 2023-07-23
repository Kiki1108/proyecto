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


    def gastar_vacunas(self, a, b, c):
        for i in self.__vacunas_restantes:
            match i:
                case 0: self.__vacunas_restantes[i] = self.__vacunas_restantes[i] - a
                case 1: self.__vacunas_restantes[i] = self.__vacunas_restantes[i] - b
                case 2: self.__vacunas_restantes[i] = self.__vacunas_restantes[i] - c
