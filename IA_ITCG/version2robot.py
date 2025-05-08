import tkinter as tk
import random

tk_width = 600
tk_height = 400
robot_size = 20
battery_max = 100
num_basura = 10

class RobotRecogedor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.robot = self.canvas.create_rectangle(50, 50, 50+robot_size, 50+robot_size, fill='blue')
        self.battery = battery_max
        self.battery_text = self.canvas.create_text(50, 10, text=f"Batería: {self.battery}%", anchor="nw", font=("Arial", 12))
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])
        self.basura = []
        self.deposito = self.canvas.create_rectangle(30, tk_height - 50, 50, tk_height - 30, fill='red')
        self.carga = self.canvas.create_rectangle(tk_width - 50, tk_height - 50, tk_width - 30, tk_height - 30, fill='green')
        self.tiene_basura = False
        self.pasos = 0
        self.colocar_basura()
        self.move_robot()
    
    def colocar_basura(self):
        for _ in range(num_basura):
            x, y = random.randint(50, tk_width-50), random.randint(50, tk_height-50)
            obj = self.canvas.create_oval(x, y, x+10, y+10, fill='brown')
            self.basura.append((obj, x, y))
    
    def move_robot(self):
        if self.battery <= 0:
            return
        
        x1, y1, x2, y2 = self.canvas.coords(self.robot)
        
        if self.battery <= 30 and not self.tiene_basura:
            self.ir_a_carga(x1, y1)
        elif self.tiene_basura:
            self.ir_a_deposito(x1, y1)
        else:
            self.movimiento_normal(x1, y1)
        
        self.pasos += 5
        if self.pasos >= 30:
            self.battery -= 1
            self.pasos = 0
        self.canvas.itemconfig(self.battery_text, text=f"Batería: {self.battery}%")
        
        for obj, bx, by in self.basura:
            if abs(x1 - bx) < 10 and abs(y1 - by) < 10:
                self.canvas.delete(obj)
                self.basura.remove((obj, bx, by))
                self.tiene_basura = True
                break
        
        if self.tiene_basura and x1 < 60 and y1 > tk_height - 60:
            self.tiene_basura = False
        
        if not self.tiene_basura and x1 > tk_width - 60 and y1 > tk_height - 60:
            self.battery = battery_max
            self.canvas.itemconfig(self.battery_text, text=f"Batería: {self.battery}%")
        
        self.canvas.after(50, self.move_robot)
    
    def ir_a_carga(self, x1, y1):
        if x1 < tk_width - 40:
            self.canvas.move(self.robot, 5, 0)
        elif y1 < tk_height - 40:
            self.canvas.move(self.robot, 0, 5)
    
    def ir_a_deposito(self, x1, y1):
        if x1 > 40:
            self.canvas.move(self.robot, -5, 0)
        elif y1 < tk_height - 40:
            self.canvas.move(self.robot, 0, 5)
    
    def movimiento_normal(self, x1, y1):
        if x1 + self.dx < 0 or x1 + self.dx > tk_width:
            self.dx = -self.dx
        if y1 + self.dy < 0 or y1 + self.dy > tk_height:
            self.dy = -self.dy
        self.canvas.move(self.robot, self.dx, self.dy)


root = tk.Tk()
root.title("Robot Recogedor de Basura")
canvas = tk.Canvas(root, width=tk_width, height=tk_height, bg='white')
canvas.pack()

robot = RobotRecogedor(canvas)
root.mainloop()
