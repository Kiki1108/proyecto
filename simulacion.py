import random

from enfermedad import Enfermedad
from comunidad import Comunidad
from personas import Persona

class Simulacion():
    def __init__(self, dias, comunidad, enfermedad):
        self.__dias = dias                  # int, días a durar la simulacion
        self.__comunidad = comunidad        # class comunidad
        self.__enfermedad = enfermedad      # class enfermedad
        self.__contador = 0                 # int, número de pasos (dias)


    def simular(self):
        self.generar_caso_0()
        self.imprimir_inicial()

        while self.__dias != self.__contador:
            # AQUI VA TODO

            self.__contador = self.__contador + 1
            self.imprimir_datos()


    def imprimir_inicial(self):
        print("#"*50)
        print(f"Dias que dura la simulacion: {self.__dias}")
        print(f"Cantida de población: {self.__comunidad.get_num_ciudadanos()}")
        print(f"Infectividad por contacto: {self.__enfermedad.get_infectividad()}%")
        print(f"Infectividad por contacto estrecho: {self.__enfermedad.get_infectividad_estrecho()}%")
        print(f"Promedio de conexiones por persona por día: {self.__comunidad.get_conexion_fisica()}")
        print(f"Probabilidad que la conexion sea contacto estrecho: {self.__comunidad.get_prob_contacto_estrecho()}%")
        print(f"Promedio de días para pasar la enfermedad: {self.__enfermedad.get_prom_pasos()}")
        print(f"Mortalidad: {self.__enfermedad.get_mortalidad()}%")
        print("#"*50,"\n")


    def imprimir_datos(self):
        dia = self.__contador
        contagiados = self.__comunidad.get_infectados()
        enfermos = self.__comunidad.get_enfermos()
        muertos = self.__comunidad.get_muertos()

        print(f"Día: {dia}, contagiados totales: {contagiados}, enfermos: {enfermos}, muertos {muertos}")


    def generar_caso_0(self):
        cantidad_casos_0 = self.__comunidad.get_infectados()
        cantidad_poblacion = self.__comunidad.get_num_ciudadanos()
        ciudadanos = self.__comunidad.get_ciudadanos()
        
        for i in range(cantidad_casos_0):
            while True:
                id = random.randint(0, cantidad_poblacion)
                if ciudadanos[id].get_estado() == "S":
                    ciudadanos[id].set_estado("E")
                    break
                else:
                    id = None
        self.__comunidad.set_ciudadanos(ciudadanos)