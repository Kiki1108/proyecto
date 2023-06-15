import random

# Esta clase representa la enfermedad que estara en la simulacion
class Enfermedad():
    def __init__(self, infeccion_probable, infeccion_estrecho, promedio_pasos, mortalidad):
        """
        infeccion_probable -> int, procentaje de infección para contactos no estrecho
        infeccion_estrecho -> int, porcentaje de infección para contactos estrechos
        promedio_pasos -> int, número de pasos para ser declarado sano o muerto
        mortalidad -> int, procentaje de mortalidad para el enfermo
        """
        self.__infeccion_probable = infeccion_probable
        self.__infeccion_estrecho = infeccion_estrecho
        self.__promedio_pasos = promedio_pasos
        self.__mortalidad = mortalidad


    def get_infectividad(self):
        return self.__infeccion_probable


    def get_infectividad_estrecho(self):
        return self.__infeccion_estrecho


    def get_prom_pasos(self):
        return self.__promedio_pasos


    def get_mortalidad(self):
        return self.__mortalidad


    def establecer_contador(self):
        while True:
            a = int(random.gauss(self.__promedio_pasos, self.__promedio_pasos/2))
            if a > 0:
                return a


    def is_muerto(self):
        a = random.randint(0, 100)
        if a <= self.__mortalidad:
            return True
        return False


    def is_contacto_estrecho_contagiado(self):
        a = random.randint(0, 100)
        if a <= self.__infeccion_estrecho:
            return True
        return False


    def is_contagiado(self):
        a = random.randint(0, 100)
        if a <= self.__infeccion_probable:
            return True
        return False
