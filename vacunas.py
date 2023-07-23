class Vacunas():
    def __init__(self, inicio, total, tasa, inmunidades):
        """
        Inicializa los valores de la clase Vacuna
        
        Atributos:
            inicio[int]: Día en que se empieza a entregar la vacuna
            total [int]: Total de personas
            tasa [int]: porcentaje de personas que pueden recivir la vacuna
            inmunidades [ALGO?]: Algo???
            vacunas_restantes [list]: Cantidad de vacunas que hay por tipo
        """
        self.__inicio = inicio
        self.__total = total
        self.__tasa = tasa
        self.__inmunidades = inmunidades
        self.__vacunas_restantes = [int(total* 25/ 100), int(total*50/100), int(total*25/100)]


    def get_inicio(self):
        return self.__inicio


    def get_total(self):
        return self.__total


    def get_tasa(self):
        return self.__tasa


    def get_vacunas_restantes(self):
        return self.__vacunas_restantes


    def gastar_vacunas(self, a, b, c):
        print(a, b, c)
        self.__vacunas_restantes = [self.__vacunas_restantes[0] - a, self.__vacunas_restantes[1] - b, self.__vacunas_restantes[2] -c]
