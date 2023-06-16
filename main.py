from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad


class Main():
    def __init__(self):
        """
        Valores bases para la clase Enfermedad, Comunidad y Simulacion
        """
        # Valores para la clase Enfermedad
        infeccion_probable = 5
        infeccion_estrecho = 70
        promedio_pasos = 7
        mortalidad = 5
        enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                                promedio_pasos, mortalidad)
        # Valores para la clase Comunidad
        num_ciudadanos = 2000
        infectados = 1
        prom_conexion_fisica = 10
        prob_conexión_fisica = 10
        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            prom_conexion_fisica, prob_conexión_fisica)
        # Valores para la clase Comunidad
        dias_simulacion = 60
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)
        #Se hace la simulacion
        simulacion.simular()


if __name__ == "__main__":
    main = Main()
