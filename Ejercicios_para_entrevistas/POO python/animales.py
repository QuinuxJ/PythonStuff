class Animal:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def hablar(self):
        pass
    
class Perro(Animal):
    def __init__(self, nombre, age, raza):
        super().__init__(nombre, age)
        self.raza = raza
        print(f"Perro creado: {self.name} de {self.age} Años y raza: {self.raza}")
    
    def hablar(self):
        return "GUAU!!!"
            
perro = Perro("Zeus",19,"Belgian mallinois") 
print("Y dice",perro.hablar()) 