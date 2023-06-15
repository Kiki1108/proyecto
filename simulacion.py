import random
from enfermedad import Enfermedad
from comunidad import Comunidad
from personas import Persona

class Simulacion():
    def __init__(self, dias, comunidad, enfermedad):
        # int, días a durar la simulacion
        self.__dias = dias
        # class comunidad
        self.__comunidad = comunidad
        # class enfermedad
        self.__enfermedad = enfermedad
        # int, número de pasos (dias)
        self.__contador = 0


    def simular(self):
        self.generar_caso_0()
        self.imprimir_inicial()

        #será mejor un for?
        while self.__dias != self.__contador:
            if self.__contador != 0:
                self.pasar_el_dia()
            self.__contador = self.__contador + 1
            self.imprimir_datos()


    def pasar_el_dia(self):
        self.siguen_enfermos()
        self.contagiar()
        self.leer_datos()


    def siguen_enfermos(self):
        for ciudadano in self.__comunidad.get_ciudadanos():
            if ciudadano.get_estado() == "E":
                ciudadano.restar_contador()
                if ciudadano.get_contador() == 0:
                    if self.__enfermedad.is_muerto():
                        ciudadano.set_estado("M")
                    else:
                        ciudadano.set_estado("I")


    def contagiar(self):
        lista_nuevos_enfermos = []
        for ciudadano in self.__comunidad.get_ciudadanos():
            if ciudadano.get_estado() == "E":
                conexiones = self.__comunidad.cantidad_conexiones()
                for conexion in range(conexiones):
                    if self.__comunidad.is_contacto_estrecho():
                        if self.__enfermedad.is_contacto_estrecho_contagiado():
                            lista_nuevos_enfermos.append(self.__comunidad.contagiar_contacto_estrecho(ciudadano))
                    else:
                        if self.__enfermedad.is_contagiado():
                            lista_nuevos_enfermos.append(self.__comunidad.contagiar_random())
        for _id in lista_nuevos_enfermos:
            for ciudadano in self.__comunidad.get_ciudadanos():
                if ciudadano.get_id()[3:8] == _id:
                    ciudadano.set_estado("E")
                    ciudadano.set_contador(self.__enfermedad.establecer_contador())
                    break


    def leer_datos(self):
        muertos = 0
        enfermos = 0
        inmunes = 0
        suceptibles = 0
        for ciudadano in self.__comunidad.get_ciudadanos():
            match ciudadano.get_estado():
                case "M": muertos += 1
                case "E": enfermos += 1
                case "I": inmunes += 1
                case "S": suceptibles += 1
        self.__comunidad.set_muertos(muertos)
        self.__comunidad.set_enfermos(enfermos)
        self.__comunidad.set_infectados(muertos+enfermos+inmunes)

        # leer los datos de la poblacion (o actualizarlos)
        # contagiados nuevos, enfermos actuales, muertos
        pass


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

        print(f"Día: {dia}, contagiados totales: {contagiados}, enfermos: {enfermos}, muertos {muertos}\n")


    def generar_caso_0(self):
        cantidad_casos_0 = self.__comunidad.get_infectados()
        cantidad_poblacion = self.__comunidad.get_num_ciudadanos()
        ciudadanos = self.__comunidad.get_ciudadanos()

        for _ in range(cantidad_casos_0):
            while True:
                id = random.randint(0, cantidad_poblacion)
                if ciudadanos[id].get_estado() == "S":
                    ciudadanos[id].set_estado("E")
                    ciudadanos[id].set_contador(self.__enfermedad.establecer_contador())
                    break
                else:
                    id = None
        self.__comunidad.set_ciudadanos(ciudadanos)
