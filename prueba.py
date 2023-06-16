# prueba de distribucion
"""
import numpy as np
import statsmodels.api as sm
import pylab as py
  
# np.random generates different random numbers
# whenever the code is executed
# Note: When you execute the same code 
# the graph look different than shown below.
  
# Random data points generated
data_points = np.random.normal(0, 1, 100)
  
sm.qqplot(data_points, line ='45')
py.show()
"""


# Prueba de gráficos
"""
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y1 = [10,2,5,6,7,2,99,10,1,0]

plt.plot(x,y1)
plt.grid()              # rejilla
plt.xlabel('Días')
plt.ylabel('Población')
plt.title('Uwu')
print(type(plt))
plt.show()
"""


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