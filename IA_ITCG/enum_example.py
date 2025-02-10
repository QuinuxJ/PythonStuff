from enum import Enum, auto

class Numeros(Enum):
    # auto() asigna un valor automatico a cada elemento de la enumeracion, iniciando con 1
    UNO = auto()
    DOS = auto()
    TRES = auto()
    CUATRO = auto()
    CINCO = auto()

# los valores definidos son los miembros de enumeracion, para acceder a ellos
# hay que relacionarlos con el nombre del a enumeracion Numeros.UNO., Numeros.DOS
# un dato enumerado estara compuesto de dos parte: nombre y valor
# UNO es el nombre, y el valor que le asigna auto() es la representacion de valor de ese enum
print(Numeros.DOS)
print(repr(Numeros.DOS))
print(type(Numeros.DOS))
print(isinstance(Numeros.DOS, Numeros))
print(Numeros.DOS.name)
print(Numeros.DOS.value)

for i in Numeros:
    print(i) 