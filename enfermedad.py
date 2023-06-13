import random

class Enfermedad():
    def __init__(self, infeccion_probable, infeccion_estrecho, promedio_pasos, mortalidad):
        self.__infeccion_probable = infeccion_probable      # int, procentaje de infección para no contacto estrecho
        self.__infeccion_estrecho = infeccion_estrecho      # int, porcentaje de infección para contactos estrechos
        self.__promedio_pasos = promedio_pasos              # int, número de pasos para ser declarado sano o muerto
        self.__mortalidad = mortalidad                      # int, procentaje de mortalidad para el enfermo


    def get_infectividad(self):
        return self.__infeccion_probable


    def get_infectividad_estrecho(self):
        return self.__infeccion_estrecho
    
    
    def get_prom_pasos(self):
        return self.__promedio_pasos
    

    def get_mortalidad(self):
        return self.__mortalidad
    

    def siguie_enfermo(self):
        while True:
            a = random.gauss(self.__promedio_pasos, self.__promedio_pasos/2)
            if a >= 0:
                if int(a) == 0:
                    return False
                else:
                    return True
    

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