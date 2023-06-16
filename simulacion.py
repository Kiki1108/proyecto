import random
# En ningun momento son usados estos imports -LONDRO
from enfermedad import Enfermedad
from comunidad import Comunidad
from personas import Persona

class Simulacion():
    def __init__(self, dias, comunidad, enfermedad):
        """
        Inicializa los valores de la clase Simulacion
        
        Atributos:
            dias [int]: Número de días que dura la simulación
            comunidad [Comunidad]: Comunidad en la simulación
            enfermedad [Enfermedad]: Número de fermetos a m
            contador [int]: Representa los dias que esta o estan pasando
        """
        self.__dias = dias
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad
        self.__contador = 0


    def simular(self):
        """
        Genera la simulación de inicial y puede pasar el
        """
        self.generar_caso_0()
        self.imprimir_inicial()

        #será mejor un for? -Cristian, supongo
        # Yo creo que si -LONDRO
        # una wea tipo "For dia in range(0, self.dias)"
        while self.__dias != self.__contador:
            # Cambia de día en la simulación
            if self.__contador != 0:
                self.pasar_el_dia()
            self.__contador = self.__contador + 1
            self.imprimir_datos()


    def pasar_el_dia(self):
        """
        Cerra la ventana y sigue a los enfermos.
        """
        self.siguen_enfermos()
        self.contagiar()
        self.leer_datos()


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
        lista_nuevos_enfermos = []
        for ciudadano in self.__comunidad.get_ciudadanos():
            # Demuestra el contagio generado en la comunidad
            if ciudadano.get_estado() == "E":
                conexiones = self.__comunidad.cantidad_conexiones()
                for _ in range(conexiones):    # _ Representa cada conexion que tiene la persona
                    if self.__comunidad.is_contacto_estrecho():
                        if self.__enfermedad.is_contacto_estrecho_contagiado():
                            lista_nuevos_enfermos.append(self.__comunidad.contagiar_contacto_estrecho(ciudadano))
                    else:
                        if self.__enfermedad.is_contagiado():
                            lista_nuevos_enfermos.append(self.__comunidad.contagiar_random())
        for _id in lista_nuevos_enfermos:
            for ciudadano in self.__comunidad.get_ciudadanos():
                # Consigue todos los nuevos enfermos y cambia su estado
                if ciudadano.get_id()[3:8] == _id:
                    ciudadano.set_estado("E")
                    ciudadano.set_contador(self.__enfermedad.establecer_contador())
                    break


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
        self.__comunidad.set_enfermos(enfermos)
        self.__comunidad.set_infectados(muertos+enfermos+inmunes)
        pass


    def imprimir_inicial(self):
        """
        Imprimir la información de inicialización de la simulación.
        """
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
            # Poner que hace -LONDRO
            while True:
                id = random.randint(0, cantidad_poblacion)
                # Poner que hace -LONDRO
                if ciudadanos[id].get_estado() == "S":
                    ciudadanos[id].set_estado("E")
                    ciudadanos[id].set_contador(self.__enfermedad.establecer_contador())
                    break
                else:
                    id = None
        self.__comunidad.set_ciudadanos(ciudadanos)
