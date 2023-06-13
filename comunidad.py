import json
import random

from enfermedad import Enfermedad
from personas import Persona

with open("nombres_apellidos.json") as archivo:
    dic = json.load(archivo)

class Comunidad():
    def __init__(self, num_ciudadanos, enfermedad, infectados, prom, prob):
        self.__num_ciudadanos = num_ciudadanos      # int, cantidad todal de la población de la comunidad
        self.__enfermedad = enfermedad              # class Enfermedad
        self.__ciudadanos = self.hacer_poblacion()  # [class Persona], las personas de la comunidad
        self.__infectados = infectados              # int, número de infectados totales
        self.__enfermos = infectados                # int, indica el número de infectados actuales
        self.__muertos = 0                          # int, indica el número de muertos totales
        self.__prom_conexion_fisica = prom          # int, indica el prom de conecciones físicas que tiene una persona
        self.__prob_conexion_fisica = prob          # int, indica la prob que el contacto físico sea un contacto estrecho


    def get_num_ciudadanos(self):
        return self.__num_ciudadanos


    def get_infectados(self):
        return self.__infectados


    def get_ciudadanos(self):
        return self.__ciudadanos
    

    def get_enfermos(self):
        return self.__enfermos
    

    def get_muertos(self):
        return self.__muertos
    

    def get_conexion_fisica(self):
        return self.__prom_conexion_fisica
    

    def get_prob_contacto_estrecho(self):
        return self.__prob_conexion_fisica


    def set_ciudadanos(self, ciudadanos):
        self.__ciudadanos = ciudadanos
    

    def set_muertos(self, muertos):
        self.__muertos = muertos


    def set_enfermos(self, enfermos):
        self.__enfermos = enfermos


    def set_infectados(self, infectados):
        self.__infectados = infectados


    def contagiar_contacto_estrecho(self, persona):
        for ciudadano in self.__ciudadanos:
            for palabra in ciudadano.get_nombre():
                if palabra in persona.get_nombre():
                    if ciudadano.get_estado() == "S":
                        return ciudadano.get_id()
                    elif ciudadano.get_estado() in ["E", "I"]:
                        return None
                    
    
    def contagiar_random(self):
        while True:
            id = random.randint(0, self.__num_ciudadanos)
            for ciudadano in self.__ciudadanos:
                if ciudadano.get_id() == id:
                    if ciudadano.get_estado() == "S":
                        return id
                    elif ciudadano.get_estado() in ["E", "I"]:
                        return None


    def is_contacto_estrecho(self):
        random_number = random.randint(0, 100)
        if random_number <= self.__prob_conexion_fisica:
            return True
        return False


    def cantidad_conexiones(self):
        while True:
            conexiones = random.gauss(self.__prom_conexion_fisica, self.__prom_conexion_fisica/2)
            if conexiones >= 0:
                break
        return int(conexiones)


    def hacer_poblacion(self):
        lista = []

        for i in range(self.__num_ciudadanos):
            id = i
            nombre = dic["nombres"][random.randint(0, len(dic["nombres"])-1)]
            apellido1 = dic["apellidos"][random.randint(0, len(dic["apellidos"])-1)]
            apellido2 = dic["apellidos"][random.randint(0, len(dic["apellidos"])-1)]
            enfermedad = self.__enfermedad
            estado = "S"    # valor incial en suceptible

            persona = Persona(id, [nombre, apellido1, apellido2], enfermedad, estado)
            lista.append(persona)

        return lista


