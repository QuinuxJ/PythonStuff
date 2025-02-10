from enum import Enum
class Colores(Enum):
    BLANCO = 7
    ROJO = 4
    NEGRO = 9
    AZUL = 3
    LIMON = 10
    CAFE = 5
    WHITE =7
    RED=4
    BLACK=9
    BLUE=3
    LEMON=10
    BROWN=5
for c in Colores:
    print(c)
    
print()
print(Colores.BLANCO)
print(Colores.WHITE)
print(Colores(7))
print(Colores(3))
print(Colores['NEGRO'])
print(Colores['BLACK'])
negro=Colores.BLACK
print(negro)
lista=list(Colores)
print(lista)
tupla=tuple(Colores)
print(tupla)