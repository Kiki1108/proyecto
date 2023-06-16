import random

class Enfermedad():
    def __init__(self, infeccion_probable, infeccion_estrecho, promedio_pasos, mortalidad):
        """
        Inicializa los valores de la clase Enfermedad
        
        Atributos:
            infeccion_probable [int]: La probabilidad de la infeccion a un persona
            infeccion_estrecho [int]: La probabilidad de la infeccion a un contacto estrecho
            promedio_pasos [int]: Los pasos (días) que debe desarollarse la enfermedad
            mortalidad [int]: La mortalidad de la enfermedad
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
        """
        Genera la cantidad de pasos que deberia tener cada persona una vez enfermada
        
        Retorna:
            Número de pasos que tendra la persona
        """
        while True:
            a = int(random.gauss(self.__promedio_pasos, self.__promedio_pasos/2))
            if a > 0:
                return a


    def is_muerto(self):
        """
        Define si la persona se murio, o no
        
        Retorna: 
            True si se murio, False si no se murio
        """
        a = random.randint(0, 100)
        if a <= self.__mortalidad:
            return True
        return False


    def is_contacto_estrecho_contagiado(self):
        """
        Determina si es un contacto estrecho
        
        Retorna: 
            True si es contacto estrecho, False si no lo es
        """
        a = random.randint(0, 100)
        if a <= self.__infeccion_estrecho:
            return True
        return False


    def is_contagiado(self):
        """
        Determina si el contagio es activo para infectar a otra persona

        Retorna:
            True si puede ser contagiado, False si no
        """
        a = random.randint(0, 100)
        if a <= self.__infeccion_probable:
            return True
        return False
