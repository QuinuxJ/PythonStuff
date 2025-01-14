class Coche:
    
    def __init__(self,marca,modelo,anio,color,velocidad):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.velocidad = velocidad
        
    def mostrarDatos(self):
        print(f"Datos del auto:\nMarca {self.marca}\nModelo: {self.modelo}\nAnio: {self.anio}\nColor: {self.color}\nVelocidad: {self.velocidad}\n")
        
    def acelerar(self):
        self.velocidad = self.velocidad + 10
        print(f"La nueva velociad tras acelerar es: {self.velocidad}")
        
    def frenar(self):
        self.velocidad = self.velocidad - 10
        print(f"La nueva velociad tras frenar es: {self.velocidad}")
        
auto1 = Coche("Mazda","MX-5",2017,"Rojo",70)
auto2 = Coche("BWM","CHACHAU",2015,"Verde",90)

auto1.acelerar()
auto2.frenar()
auto1.mostrarDatos()
auto2.mostrarDatos()