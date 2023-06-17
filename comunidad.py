import json
import random

from personas import Persona

# Abre el archivo con los posibles nombres y apellidos de las personas
with open("nombres_apellidos.json") as archivo:
    dic = json.load(archivo)


class Comunidad():
    def __init__(self, num_ciudadanos, enfermedad, infectados, prom, prob):
        """
        Inicializa los valores de la clase Comunidad

        Atributos:
            num_ciudadanos [int]: Número de ciudadanos
            enfermedad [Enfermedad]: Enfermedad que esta en la comunidad
            infectados [int]: Cantidad de infectados que hay
            prom [int]: Media de generar una conexion fisica
            prob [int]: Probabilidad de generar una conexión fisica
            ciudadanos [list(Persona)]: Las personas de la comunidad
            familas [dict(Persona)]: Las personas de la comunidad agrupadas en familias
            muertos [int]: Indica el número de muertos totales
        """
        self.__num_ciudadanos = num_ciudadanos
        self.__infectados = infectados    # Cantidad de infectados (Personas con estados: E, I, M)
        self.__enfermos = infectados    # Cantidad de enfermos (Personas con estado: E)
        self.__enfermedad = enfermedad
        self.__prom_conexion_fisica = prom
        self.__prob_conexion_fisica = prob
        self.__ciudadanos = []
        self.__familias = {}
        self.__muertos = 0
        #Funciones de inicio
        self.hacer_poblacion()
        self.hacer_familias()


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
        """
        Contagiar un ciudadano posiblemente cercano. Cuando el estado de "S" devuelve el _id

        Argumentos:
            persona: Persona que esta enferma

        Retorna:
            Un _id
        """
        for familia in self.__familias:
            if persona.get_id()[0:3] == familia:
                familia_actual = self.__familias[familia]
                index = random.randint(0, len(familia_actual) - 1)
                if familia_actual[index] != persona and familia_actual[index].get_estado() == "S":
                    familia_actual[index].set_estado("E")
                    familia_actual[index].set_contador(self.__enfermedad.establecer_contador())
                    return None
                elif familia_actual[index] != persona and familia_actual[index].get_estado() in ["E", "I"]:
                    return None


    def contagiar_random(self):
        """
        Contagiar un ciudadano aleatorio. Cuando el estado de "S" devuelve el _id

        Retorna:
            Un _id
        """
        while True:
            _id = random.randint(0, self.__num_ciudadanos - 1)
            ciudadano = self.__ciudadanos[_id]
            if ciudadano.get_estado() == "S":
                ciudadano.set_estado("E")
                ciudadano.set_contador(self.__enfermedad.establecer_contador())
                break
            elif ciudadano.get_estado() in ["E", "I"]:
                break

    def is_contacto_estrecho(self):
        """
        Determina si ehay probabilidad de conexion fisica en un contacto estrecho

        Retorna:
            True si el usuario estrecho, False si no lo es
        """
        random_number = random.randint(1, 100)
        if random_number <= self.__prob_conexion_fisica:
            return True
        return False


    def cantidad_conexiones(self):
        """
        Genera la cantidad de conexines que puede tener una persona

        Retorna:
            La cantidad de conexiones
        """
        while True:
            conexiones = random.gauss(self.__prom_conexion_fisica, self.__prom_conexion_fisica/2)
            if conexiones >= 0:
                break
        return int(conexiones)


    def generar_id(self, i, apellido):
        """
        Genera el identificador de la persona segun su apellido y numero de generacion

        Argumentos:
            i: El número de generación
            apellido: El algoritmo de la que se desea generar el identificador

        Retorna:
            Un _id para una persona
        """
        _id = str(i)
        largo = len(_id)
        l_deseado = (len(str(self.__num_ciudadanos)) - 1) + 3
        while largo != l_deseado:
            # si tiene menos de 5 digitos los rellena y luego adjunta al inicio el codigo correspondiente al apellido
            if largo == l_deseado - 3:
                _id = f"{apellido}{_id}"
                largo = len(_id)
            else:
                _id = f"0{_id}"
                largo = len(_id)
        return _id


    def hacer_poblacion(self):
        """
        Método que hace una población de la comunidad
        """
        lista = []
        for i in range(self.__num_ciudadanos):
            # Genera una persona por iteracion
            nombre = dic["nombres"][random.randint(0, len(dic["nombres"])-1)]
            indice_apellido = random.randint(0, len(dic["apellidos"]) - 1)
            apellido1 = dic["apellidos"][indice_apellido]
            apellido2 = dic["apellidos"][random.randint(0, len(dic["apellidos"])-1)]
            _id = self.generar_id(i, indice_apellido)
            persona = Persona(_id, [nombre, apellido1, apellido2])
            lista.append(persona)
        self.__ciudadanos = lista


    def hacer_familias(self):
        """
        Método que hace las familias de la comunidad
        """
        for persona in self.__ciudadanos:
            if persona.get_id()[0:3] in self.__familias:
                self.__familias[persona.get_id()[0:3]].append(persona)
            else:
                self.__familias[persona.get_id()[0:3]] = [persona]