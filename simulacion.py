import random
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

from time import sleep

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
        #
        self.escritura = ""

        # uwu
        self.__infectados_array = [self.__comunidad.get_infectados()]
        self.__enfermos_array = [self.__comunidad.get_infectados()]
        self.__muertos_array = [0]
        self.__suceptibles_array = [self.__comunidad.get_num_ciudadanos()]


    def get_dias(self):
        return self.__dias
    

    def get_contador(self):
        return self.__contador
    

    def avanzar_contador(self):
        self.__contador = self.__contador + 1
    

    def simular(self):
        self.generar_caso_0()
        self.imprimir_inicial()
        sleep(1)

        # será mejor un for?
        while self.__dias != self.__contador:
            if self.__contador != 0:
                self.pasar_el_dia()
            self.__contador = self.__contador + 1
            self.imprimir_datos()
            #if not self.__contador % 10 and self.__contador != self.__dias:
            #    self.mostrar_grafico()
        self.mostrar_grafico()
        self.mostrar_dis()
        


    def pasar_el_dia(self):
        self.siguen_enfermos()
        self.contagiar()
        self.leer_datos()


    def mostrar_dis(self):
        data_points = np.array(self.__enfermos_array)
        sm.qqplot(data_points, line='s')
        plt.show()


    def mostrar_grafico(self):
        x = []
        for i in range(self.__contador):
            x.append(i+1)
        plt.plot(x,self.__enfermos_array)
        plt.plot(x,self.__infectados_array)
        plt.plot(x,self.__muertos_array)
        plt.plot(x,self.__suceptibles_array)
        plt.grid()              # rejilla
        plt.xlabel('Días')
        plt.ylabel('Población')
        if self.__dias == self.__contador:
            plt.title(f"Gráfico Modelo SIR Final de la sumlación ({self.__dias} días)")
        else:
            plt.title(f"Gráfico Modelo SIR día {self.__contador}")
        plt.show()
        

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
                            pass
                    else:
                        if self.__enfermedad.is_contagiado():
                            lista_nuevos_enfermos.append(self.__comunidad.contagiar_random())
                            pass
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
        self.__muertos_array.append(muertos)
        self.__comunidad.set_enfermos(enfermos)
        self.__enfermos_array.append(enfermos)
        self.__comunidad.set_infectados(muertos+enfermos+inmunes)
        self.__infectados_array.append(muertos+enfermos+inmunes)
        self.__suceptibles_array.append(suceptibles)

        # leer los datos de la poblacion (o actualizarlos)
        # contagiados nuevos, enfermos actuales, muertos


    def imprimir_inicial(self):
        a = f"""
######################################################
Dias que dura la simulacion: {self.__dias}
Cantida de población: {self.__comunidad.get_num_ciudadanos()}
Infectividad por contacto: {self.__enfermedad.get_infectividad()}%
Infectividad por contacto estrecho: {self.__enfermedad.get_infectividad_estrecho()}%
Promedio de conexiones por persona por día: {self.__comunidad.get_conexion_fisica()}
Probabilidad que la conexion sea contacto estrecho: {self.__comunidad.get_prob_contacto_estrecho()}%
Promedio de días para pasar la enfermedad: {self.__enfermedad.get_prom_pasos()}
Mortalidad: {self.__enfermedad.get_mortalidad()}%
######################################################
        """
        print(a)


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
