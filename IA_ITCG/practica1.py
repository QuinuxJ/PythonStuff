def perimetroArea(lado):
    perimetro = lado * 4
    area = lado * lado
    
    return f"el perimetro del cuadrado es: {perimetro} y el area es: {area:.3f}"
try:
  lado = float(input("Ingresa el valor de lado de tu cuadrado: "))
  print(perimetroArea(lado))
except:
  print('Introduce un valor correcto')
