from enum import Enum

class Sabor(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MENTA = 3
    LIMON = 10
    NUEZ = 5

for sabor in Sabor:
    print(sabor)

#acceso direto al enum, siempre y cuando nos sepamos su valor
print()
print(Sabor(7))
print(Sabor(3))
print(Sabor['CHOCOLATE'])
print(Sabor['LIMON'])
#se puede asignar un miembro de la enum a una variable
print()
nieve=Sabor.CHOCOLATE
print(nieve)
print(nieve.name)
print(nieve.value)