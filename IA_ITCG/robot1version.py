import tkinter as tk
import random

tk_width = 600
tk_height = 400
robot_size = 20
battery_max = 200

class RobotRecogedor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.robot = self.canvas.create_rectangle(50, 50, 50+robot_size, 50+robot_size, fill='blue')
        self.battery = battery_max
        self.battery_text = self.canvas.create_text(50, 10, text=f"Batería: {self.battery}%", anchor="nw", font=("Arial", 12))
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])
        self.move_robot()
    
    def move_robot(self):
        if self.battery <= 0:
            return
        
        x1, y1, x2, y2 = self.canvas.coords(self.robot)
        
        
        if x1 + self.dx < 0 or x2 + self.dx > tk_width:
            self.dx = -self.dx
        if y1 + self.dy < 0 or y2 + self.dy > tk_height:
            self.dy = -self.dy
        
        self.canvas.move(self.robot, self.dx, self.dy)
        self.battery -= 1
        self.canvas.itemconfig(self.battery_text, text=f"Batería: {self.battery}%")
        self.canvas.after(50, self.move_robot) 


root = tk.Tk()
root.title("Robot Recogedor de Basura")
canvas = tk.Canvas(root, width=tk_width, height=tk_height, bg='white')
canvas.pack()

robot = RobotRecogedor(canvas)
root.mainloop()
