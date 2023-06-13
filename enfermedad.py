

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