
# preuba meteodos de listas
"""
lista1 = ["Hola", "Mundo", "UWU"]
lista2 = ["Chao", "Gente", "Mundo"]

for elemento in lista1:
    if elemento in lista2:
        print("Si")
        break
    else:
        print("NO")
"""


#prueba con el random para conseguir la distribución normal
"""
import random

lista = []
for i in range(1000):
    while True:
        a = random.gauss(10, 5)
        if a > 1:
            break
    lista.append(int(a))

print(lista)
sum = 0
for i in range(25):
    a = lista.count(i)
    print("|"*a)
    sum += a
print(sum)
   # print(lista.count(i))

#for i in range(0, len(lista)):
"""


# prueba con el json para ver los nombres y apellidos
"""
import json
import random

from enfermedad import Enfermedad
from personas import Persona

with open("nombres_apellidos.json") as archivo:
    dic = json.load(archivo)

for i in range(10000):
    persona = Persona()
    a = dic["nombres"][random.randint(0, len(dic["nombres"])-1)]
    print(a)

"""