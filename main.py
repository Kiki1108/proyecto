from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad
from personas import Persona


def main():
    # Realizar la enfermedad
    infeccion_probable = 5      # int, procentaje de infeccion para no contacto estrecho
    infeccion_estrecho = 90     # int, porcentaje de infeccion para contactos estrechos
    promedio_pasos = 10         # int, numero de pasos para ser declarado vivo o muerta
    mortalidad = 10             # int, procentaje de mortalidad para el enfermo

    enfermedad = Enfermedad(infeccion_probable, infeccion_estrecho,
                            promedio_pasos, mortalidad)
    
    # Realizar la comunidad
    
    comunidad = Comunidad(enfermedad=enfermedad)



if __name__ == "__main__":
    main()