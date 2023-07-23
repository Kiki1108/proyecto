import io
import random
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from PIL import Image
plt.switch_backend('tkagg')
from gi.repository import GLib, GdkPixbuf

from personas import Persona


class Simulacion():
    def __init__(self, dias, comunidad, enfermedad, vacunas):
        """
        Inicializa los valores de la clase Simulacion

        Atributos:
            comunidad [Comunidad]: Comunidad en la simulación
            enfermedad [Enfermedad]: Número de fermetos a m
            dias [int]: Número de días que dura la simulación
            contador [int]: Representa los dias que esta o estan pasando
            infectados_array [list(int)]: Lista de cantidad deinfectados por dia
            enfermos_array [list(int)]: Lista de cantidad de enfermos por dia
            muertos_array [list(int)]: Lista de cantidad de muertos por dia
            suceptibles_array [list(int)]: Lista de cantidad de suceptibles por dia
        """
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad
        self.__dias = dias
        self.__vacunas = vacunas
        self.__contador = 0
        self.__infectados_array = [self.__comunidad.get_infectados()]
        self.__enfermos_array = [self.__comunidad.get_infectados()]
        self.__muertos_array = [0]
        self.__suceptibles_array = [self.__comunidad.get_num_ciudadanos() - self.__comunidad.get_infectados()]


    def get_dias(self):
        return self.__dias


    def get_contador(self):
        return self.__contador


    def avanzar_contador(self):
        """
        Avanza el contador, el cual representa los dias
        """
        self.__contador = self.__contador + 1


    def simular(self):
        """
        Genera la simulación de inicial y puede pasar el
        """
        for _ in range(self.__dias):
            if self.__contador == 0:
                self.generar_caso_0()
                sleep(2)
                # Cambia de día en la simulación
            elif self.__contador != 0:
                self.pasar_el_dia()
            self.__contador += 1
            self.imprimir_datos()


    def pasar_el_dia(self):
        """
        Cerra la ventana y sigue a los enfermos.
        """
        self.siguen_enfermos()
        self.contagiar()
        self.vacunar()
        self.leer_datos()


    def mostrar_grafico(self):
        """
        Muestra del gráfico de SIR
        """
        plt.clf()
        x = []
        for i in range(self.__contador):
            x.append(i+1)
        plt.plot(x,self.__enfermos_array)
        plt.plot(x,self.__infectados_array)
        plt.plot(x,self.__muertos_array)
        plt.plot(x,self.__suceptibles_array)
        plt.grid()    # rejilla
        plt.xlabel('Días')
        plt.ylabel('Población')
        # Método para elegir el título del grafico de la simulación
        if self.__dias == self.__contador:
            plt.title(f"Gráfico Modelo SIR Final de la sumlación ({self.__dias} días)")
        else:
            plt.title(f"Gráfico Modelo SIR día {self.__contador}")

        buf = io.BytesIO()
        plt.savefig(buf, format='png')

        im = Image.open(buf)
        buffer = GLib.Bytes.new(im.tobytes())
        gdata = GdkPixbuf.Pixbuf.new_from_bytes(buffer,
                                                GdkPixbuf.Colorspace.RGB,
                                                True, 8, im.width, im.height,
                                                len(im.getbands())*im.width)
        return gdata


    def siguen_enfermos(self):
        """
        Corresponde a lo que pasa con los enfermos cuando pasa un dia de la enfermedad
        """
        for ciudadano in self.__comunidad.get_ciudadanos():
            # Cambia el estado de los enfermos en caso respectivos de "Inmune" o "Muerto"
            if ciudadano.get_estado() == "E":
                ciudadano.restar_contador()
                if ciudadano.get_contador() == 0:
                    if self.__enfermedad.is_muerto():
                        ciudadano.set_estado("M")
                    else:
                        ciudadano.set_estado("I")


    def contagiar(self):
        """
        Método de contagio en la comunidad
        """
        nuevos_enfermos = []
        for ciudadano in self.__comunidad.get_ciudadanos():
            if ciudadano.get_estado() == "E":
                conecciones = self.__comunidad.cantidad_conecciones()
                for _ in range(conecciones):    # _ Representa cada coneccion
                    if self.__comunidad.is_contacto_estrecho():
                        if self.__enfermedad.is_contacto_estrecho_contagiado():
                            nuevo_enfermo = self.__comunidad.contagiar_contacto_estrecho(ciudadano)
                            if isinstance(nuevo_enfermo,Persona):
                                nuevos_enfermos.append(nuevo_enfermo)
                    else:
                        if self.__enfermedad.is_contagiado():
                            nuevo_enfermo = self.__comunidad.contagiar_random()
                            if isinstance(nuevo_enfermo, Persona):
                                nuevos_enfermos.append(nuevo_enfermo)
        for i in range(len(nuevos_enfermos)):
            nuevos_enfermos[i].set_estado('E')

        
    def vacunar(self):
        if self.__contador + 1 < self.__vacunas.get_inicio():
            return
        if self.__vacunas.get_vacunas_restantes()[0] <= 0:
            return

        
        vacunas = 0
        tasa = self.__vacunas.get_tasa()

        while vacunas <= 0 or vacunas > (tasa * 2 * self.__comunidad.get_num_ciudadanos()): 
            vacunas = int(random.gauss(tasa/100, tasa / 1000) * self.__comunidad.get_num_ciudadanos())

        vacunas = [int(vacunas*0.25), int(vacunas*0.5), int(vacunas*0.25)]

        self.__vacunas.gastar_vacunas(vacunas[0], vacunas[1], vacunas[2])
        print(vacunas)
        print(self.__vacunas.get_vacunas_restantes())

        


    def leer_datos(self):
        """
        Lee los datos de la comunidad y actualiza el proceso de cada
        """
        muertos = 0
        enfermos = 0
        inmunes = 0
        suceptibles = 0
        # Lee los datos de la poblacion (o los actualiza), guardandolos en la comunidad
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


    def imprimir_inicial(self):
        """
        Entrega en la terminal los datos de inicio de la simulación
        """
        print("#"*50)
        print(f"Dias que dura la simulacion: {self.__dias}")
        print(f"Cantida de población: {self.__comunidad.get_num_ciudadanos()}")
        print(f"Infectividad por contacto: {self.__enfermedad.get_infectividad()}%")
        print(f"Infectividad por contacto estrecho: {self.__enfermedad.get_infectividad_estrecho()}%")
        print(f"Promedio de conecciones por persona por día: {self.__comunidad.get_coneccion_fisica()}")
        print(f"Probabilidad que la coneccion sea contacto estrecho: {self.__comunidad.get_prob_contacto_estrecho()}%")
        print(f"Promedio de días para pasar la enfermedad: {self.__enfermedad.get_prom_pasos()}")
        print(f"Mortalidad: {self.__enfermedad.get_mortalidad()}%")
        print("#"*50,"\n")


    def imprimir_datos(self):
        """
        Imprimir los datos de la comunidad en el día en cuestion
        """
        dia = self.__contador
        contagiados = self.__comunidad.get_infectados()
        enfermos = self.__comunidad.get_enfermos()
        muertos = self.__comunidad.get_muertos()
        print(f"Día: {dia}, contagiados totales: {contagiados}, enfermos: {enfermos}, muertos {muertos}\n")


    def generar_caso_0(self):
        """
        Genera el caso 0 de la comunidad
        """
        cantidad_casos_0 = self.__comunidad.get_infectados()
        cantidad_poblacion = self.__comunidad.get_num_ciudadanos()
        ciudadanos = self.__comunidad.get_ciudadanos()
        for _ in range(cantidad_casos_0): # _ Representa cada caso inicial generado
            while True:
                id = random.randint(0, cantidad_poblacion)
                if ciudadanos[id].get_estado() == "S":
                    ciudadanos[id].set_estado("E")
                    ciudadanos[id].set_contador(self.__enfermedad.establecer_contador())
                    break
                else:
                    id = None

        self.__comunidad.set_ciudadanos(ciudadanos)
