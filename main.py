from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad


"""
Son 10 atributos a cambiar en el gtk, los 9 mencionados aqui
y el nombre de la enfermedad en la wea grafica
"""

# boxplot python 3 lineas
class Main():
    def __init__(self):
        """
        Configurar la enfermedad
        """
        # int, procentaje de infeccion para no contacto estrecho
        infeccion_probable = 5
        # int, porcentaje de infeccion para contactos estrechos
        infeccion_estrecho = 70
        # int, numero medio de pasos para ser declarado sano o muerto
        promedio_pasos = 7
        # int, procentaje de mortalidad para el enfermo
        mortalidad = 5

        enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                                promedio_pasos, mortalidad)

        """
        Configurar la comunidad
        """
        # int, cantidad de población incial
        num_ciudadanos = 2000
        # int, cantidad de infectados inciales
        infectados = 1
        # int, indica el prom de conecciones físicas que tiene una persona
        prom_conexion_fisica = 10
        # int, indica la prob que el contacto físico sea un contacto estrecho
        prob_conexión_fisica = 10

        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_conexion_fisica, prob_conexión_fisica)

        """
        Se realiza la simulación
        """
        # int, dias que dura la simulacion
        dias_simulacion = 60
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)

        simulacion.simular()


if __name__ == "__main__":
    main = Main()