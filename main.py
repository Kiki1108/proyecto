from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad


"""
LONDRO: HELLO EVERYNYAN, pondre algunas cosas aqui en cuenta:
1.- VENTANA: Son 10 atributos a cambiar en el gtk, los 9 mencionados aqui
y el nombre de la enfermedad en la wea grafica
2.- boxplot python 3 lineas
3.- Alfinal va el archivo con las weas de ventana o no?
"""


class Main():
    def __init__(self):
        """
        Valores bases para la clase Enfermedad
        """
        # int, porcentaje de infeccion para contactos no estrechos
        infeccion_probable = 5
        # int, porcentaje de infeccion para contactos estrechos
        infeccion_estrecho = 70
        # int, numero medio de pasos (días) para ser declarado sano o muerto
        promedio_pasos = 7
        # int, porcentaje de mortalidad para el enfermo
        mortalidad = 5
        #Se le entregan los valores a la clase
        enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                                promedio_pasos, mortalidad)
        """
        Valores bases para la clase Comunidad
        """
        # int, cantidad de población incial
        num_ciudadanos = 2000
        # int, cantidad de infectados inciales
        infectados = 1
        # int, indica la media de conecciones físicas que tiene una persona
        prom_conexion_fisica = 10
        # int, indica la probabiliadad que el contacto físico sea un contacto estrecho
        prob_conexión_fisica = 10
        #Se le entregan los valores a la clase
        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_conexion_fisica, prob_conexión_fisica)
        """
        Se realiza la simulación
        """
        # int, dias que dura la simulacion
        dias_simulacion = 60
        #Se le entregan los valores a la clase, como los objetos ya hechos
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)
        #Se hace la simulacion
        simulacion.simular()


if __name__ == "__main__":
    main = Main()
