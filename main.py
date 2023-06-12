from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad
from personas import Persona


def main():
    # Set parametros:
    dias_simulacion = 45 # int
    poblacion = 100000 # int, cantidad de personas simuladas
    prom_contac_estrechos = 8 # int
    inf = 10 # int, porcentaje de infectividad de gente que no es contacto estrecho
    inf_estrecho = 90 # int, porcentaje de infectividad a contactos estrechos
    dias_promedio = 10 #int, dias promedio en que se vuelve inmune o muere 
    mortalidad = 10 #int, porcentaje de mortalidad

    #generacion de clases
    enfermedad = Enfermedad(inf=inf, inf_estrecho=inf_estrecho)
    comunidad = Comunidad(poblacion=poblacion, prom_contac_estrechos=prom_contac_estrechos)
    personas = Persona()
    simulacion = Simulacion(dias= dias_simulacion)


if __name__ == "__main__":
    main()