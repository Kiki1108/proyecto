import json
import random

from personas import Persona


with open("nombres_apellidos.json") as archivo:
    # Abre el archivo con los posibles nombres y apellidos de las personas
    dic = json.load(archivo)


class Comunidad():
    def __init__(self, num_ciudadanos, enfermedad, infectados, prom, prob):
        """
        Inicializa los valores de la clase Comunidad
        
        Atributos:
            enfermedad [Enfermedad]: Enfermedad que esta en la comunidad
            num_ciudadanos [int]: Número de ciudadanos
            infectados [int]: Cantidad de infectados que hay en total
            enfermos [int]: Cantidad de enfermos que hay en el momento
            muertos [int]: Indica el número de muertos totales
            prom_coneccion_fisica [int]: Media de generar una coneccion fisica
            prob_coneccion_fisica [int]: Probabilidad de generar una coneccion fisica
            ciudadanos [list(Persona)]: Las personas de la comunidad
            familas [dict(Persona)]: Las personas de la comunidad agrupadas en familias
            largo_id_familias [???]: @Felipe que es esta wea
            vacunados_inmunes [int]: Cantidad de gente que es inmune por la vacuna
        """
        self.__enfermedad = enfermedad
        self.__num_ciudadanos = num_ciudadanos
        self.__infectados = infectados    # Cantidad de infectados (Personas con estados: E, I, M)
        self.__enfermos = infectados    # Cantidad de enfermos (Personas con estado: E)
        self.__muertos = 0
        self.__prom_coneccion_fisica = prom
        self.__prob_coneccion_fisica = prob
        self.__ciudadanos = []
        self.__familias = {}
        self.__largo_id_familias = None
        self.__vacunados_inmune = 0
        #Funciones de inicio
        self.hacer_poblacion()


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


    def get_coneccion_fisica(self):
        return self.__prom_coneccion_fisica


    def get_prob_contacto_estrecho(self):
        return self.__prob_coneccion_fisica
    

    def get_vacunados_inmune(self):
        return self.__vacunados_inmune


    def set_ciudadanos(self, ciudadanos):
        self.__ciudadanos = ciudadanos


    def set_muertos(self, muertos):
        self.__muertos = muertos


    def set_enfermos(self, enfermos):
        self.__enfermos = enfermos


    def set_infectados(self, infectados):
        self.__infectados = infectados


    def set_vacunados_inmune(self, vacunados_inmune):
        self.__vacunados_inmune = vacunados_inmune


    def contagiar_contacto_estrecho(self, persona):
        """
        Contagiar un ciudadano posiblemente cercano. Cuando el estado de "S" devuelve el _id
        
        Argumentos:
            persona: Persona que esta enferma
        
        Retorna:
            Un _id
        """
        _id = persona.get_id()[0:self.__largo_id_familias]
        familia_actual = self.__familias[_id]
        while True:
            index = random.randint(0, len(familia_actual) - 1)
            if familia_actual[index] != persona and familia_actual[index].get_estado() == "S":
                familia_actual[index].set_contador(self.__enfermedad.establecer_contador())
                return familia_actual[index]
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
                ciudadano.set_contador(self.__enfermedad.establecer_contador())
                return ciudadano
            elif ciudadano.get_estado() in ["E", "I"]:
                return None


    def is_contacto_estrecho(self):
        """
        Determina si ehay probabilidad de coneccion fisica en un contacto estrecho
        
        Retorna:
            True si el usuario estrecho, False si no lo es
        """
        random_number = random.randint(1, 100)
        if random_number <= self.__prob_coneccion_fisica:
            return True
        return False


    def cantidad_conecciones(self):
        """
        Genera la cantidad de conexines que puede tener una persona
        
        Retorna:
            La cantidad de conecciones
        """
        while True:
            conecciones = random.gauss(self.__prom_coneccion_fisica, self.__prom_coneccion_fisica/2)
            if conecciones >= 0 and conecciones < self.__prom_coneccion_fisica*2:
                break
        return int(conecciones)


    def generar_id(self, posicion, apellido, repeticion, aumento):
        """
        Genera el identificador de la persona segun su apellido y numero de generacion
        
        Argumentos:
            i: El número de generación
            apellido: El algoritmo de la que se desea generar el identificador
        
        Retorna:
            Un _id para una persona
        """
        _id = str(posicion)
        largo = len(_id)
        l_deseado = (len(str(self.__num_ciudadanos))) + aumento
        while largo != l_deseado:
            # si tiene menos de 5 digitos los rellena y luego adjunta al inicio el codigo correspondiente al apellido
            if largo == l_deseado - aumento:
                _id = f"{apellido}{_id}"
                largo = len(_id)
            elif largo == (l_deseado - aumento) + len(str(len(dic["apellidos"]))):
                _id = f"{repeticion}{_id}"
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
        i_apellido = 0
        rep = 0
        aumento = len(str((self.__num_ciudadanos // len(dic["apellidos"])))) + len(str(len(dic["apellidos"])))
        cant = random.randint(5, 20)
        for i in range(self.__num_ciudadanos):
            # Genera una persona por iteracion
            nombre = dic["nombres"][random.randint(0, len(dic["nombres"]) - 1)]
            apellido = dic["apellidos"][i_apellido]
            _id = self.generar_id(i, i_apellido, rep, aumento)
            persona = Persona(_id, [nombre, apellido])
            lista.append(persona)
            self.__ciudadanos.append(persona)
            if len(lista) == cant or i == self.__num_ciudadanos - 1:
                self.__familias[lista[0].get_id()[0:aumento]] = lista[0:len(lista)]
                lista = []
                cant = random.randint(5, 20)
                i_apellido += 1
            if i_apellido == len(dic["apellidos"]) - 1:
                rep = rep + 1
                i_apellido = 0
        self.__largo_id_familias = aumento
