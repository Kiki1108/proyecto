from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad
from personas import Persona


class Main():
    def __init__(self):
        # Realizar la enfermedad
        infeccion_probable = 5      # int, procentaje de infeccion para no contacto estrecho
        infeccion_estrecho = 70     # int, porcentaje de infeccion para contactos estrechos
        promedio_pasos = 7          # int, numero medio de pasos para ser declarado sano o muerto
        mortalidad = 5              # int, procentaje de mortalidad para el enfermo

        enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                                promedio_pasos, mortalidad)
        
        # Realizar la comunidad
        num_ciudadanos = 20000      # int, cantidad de población incial
        infectados = 1              # int, cantidad de infectados inciales
        prom_conexion_fisica = 10   # int, indica el prom de conecciones físicas que tiene una persona
        prob_conexión_fisica = 10   # int, indica la prob que el contacto físico sea un contacto estrecho

        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_conexion_fisica, prob_conexión_fisica)

        # Se realiza la simulación
        dias_simulacion = 60        # int, dias que dura la simulacion

        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)
        
        simulacion.simular()


if __name__ == "__main__":
    main = Main()