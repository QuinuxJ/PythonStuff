import tkinter as tk
import random
import math
import time

# Configuración de la ventana
root = tk.Tk()
root.title("Robot Recogedor de Basura")
root.geometry("800x600")

# Creación del Canvas
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Creación del robot (cuadrado azul)
robot_id = canvas.create_rectangle(50, 50, 90, 90, fill="blue", outline="black", width=2)

# Ubicación fija de la estación de carga y el depósito
carga_id = canvas.create_rectangle(700, 500, 750, 550, fill="green")  # Estación de carga
deposito_id = canvas.create_rectangle(50, 500, 100, 550, fill="gray")  # Depósito de basura

# Lista para almacenar la basura
basura = []

# Variables del robot
energia = 100  # Energía inicial
basura_recolectada = 0  # Contador de basura recogida
cargando = False  # Estado de recarga

# Etiqueta para mostrar la energía
energia_label = tk.Label(root, text=f"Energía: {energia}", font=("Arial", 14))
energia_label.pack()

# Función para generar basura aleatoria
def generar_basura():
    for _ in range(random.randint(10, 15)):  # Genera entre 10 y 15 basuras
        x = random.randint(50, 750)  # Evitar los bordes
        y = random.randint(50, 550)
        basura_id = canvas.create_oval(x, y, x+20, y+20, fill="brown")  # Basura como círculo
        basura.append((basura_id, random.randint(5, 15)))  # Almacena ID y peso (energía a consumir)

generar_basura()

# Función para detectar colisión con la basura
def detectar_colision():
    global energia, basura_recolectada
    x1_r, y1_r, x2_r, y2_r = canvas.coords(robot_id)

    for basura_id, peso in basura[:]:  # Iteramos sobre una copia de la lista
        x1_b, y1_b, x2_b, y2_b = canvas.coords(basura_id)

        # Si el robot toca la basura
        if (x1_r < x2_b and x2_r > x1_b) and (y1_r < y2_b and y2_r > y1_b):
            canvas.delete(basura_id)  # Eliminar basura del canvas
            basura.remove((basura_id, peso))  # Eliminar de la lista
            basura_recolectada += 1  # Incrementar contador de basura
            energia -= peso  # Consumir energía según el peso de la basura
            energia_label.config(text=f"Energía: {energia}")  # Actualizar etiqueta
            mover_hacia(50, 500, depositar_basura)  # Llevar la basura al depósito

# Función para depositar la basura en el bote
def depositar_basura():
    global basura_recolectada
    basura_recolectada = 0  # Vacía la basura
    energia_label.config(text=f"Energía: {energia}")  # Actualizar etiqueta
    mover_robot()  # Continuar con el movimiento normal

# Función para detectar colisión con la estación de carga
def detectar_carga():
    global energia, cargando

    x1_r, y1_r, x2_r, y2_r = canvas.coords(robot_id)
    x1_c, y1_c, x2_c, y2_c = canvas.coords(carga_id)

    # Si el robot toca la estación de carga
    if (x1_r < x2_c and x2_r > x1_c) and (y1_r < y2_c and y2_r > y1_c):
        cargando = True
        energia_label.config(text="Cargando... ⏳")
        root.after(3000, finalizar_carga)  # Espera 3 segundos antes de recargar

# Función para finalizar la recarga
def finalizar_carga():
    global energia, cargando
    energia = 100  # Recarga energía
    cargando = False
    energia_label.config(text=f"Energía: {energia}")  # Actualizar etiqueta
    mover_robot()  # Retomar el movimiento normal

# Función para mover el robot
def mover_robot():
    global energia, cargando

    if cargando:  # Si está cargando, no moverse
        return

    if energia <= 0:  # Si no tiene energía, ir a la estación de carga
        mover_hacia(700, 500, detectar_carga)
    else:
        basura_mas_cercana = encontrar_basura_mas_cercana()

        if basura_mas_cercana:
            mover_hacia(*basura_mas_cercana, detectar_colision)  # Ir hacia la basura
        else:
            dx = random.choice([-10, 0, 10])  # Movimiento en X
            dy = random.choice([-10, 0, 10])  # Movimiento en Y

            # Obtener coordenadas actuales
            x1, y1, x2, y2 = canvas.coords(robot_id)

            # Evitar que el robot se salga de la pantalla
            if x1 + dx < 0 or x2 + dx > 800:
                dx = -dx
            if y1 + dy < 0 or y2 + dy > 600:
                dy = -dy

            # Mover el robot
            canvas.move(robot_id, dx, dy)
            energia -= 1  # Cada movimiento gasta 1 de energía
            energia_label.config(text=f"Energía: {energia}")  # Actualizar energía en pantalla

        # Detectar si tocó basura
        detectar_colision()

    # Repetir el movimiento cada 100ms
    root.after(100, mover_robot)

# Función para mover el robot a una posición específica y luego ejecutar una acción
def mover_hacia(dest_x, dest_y, callback=None):
    x1, y1, x2, y2 = canvas.coords(robot_id)

    dx = 5 if x1 < dest_x else -5 if x1 > dest_x else 0
    dy = 5 if y1 < dest_y else -5 if y1 > dest_y else 0

    canvas.move(robot_id, dx, dy)

    if (x1, y1) != (dest_x, dest_y):  # Si no ha llegado, seguir moviéndose
        root.after(100, lambda: mover_hacia(dest_x, dest_y, callback))
    else:
        if callback:
            callback()  # Ejecutar la acción después de llegar al destino

# Función para encontrar la basura más cercana
def encontrar_basura_mas_cercana():
    x1_r, y1_r, _, _ = canvas.coords(robot_id)

    basura_mas_cercana = None
    menor_distancia = float("inf")

    for basura_id, _ in basura:
        x1_b, y1_b, _, _ = canvas.coords(basura_id)
        distancia = math.sqrt((x1_r - x1_b) ** 2 + (y1_r - y1_b) ** 2)

        if distancia < menor_distancia:
            menor_distancia = distancia
            basura_mas_cercana = (x1_b, y1_b)

    return basura_mas_cercana

# Iniciar el movimiento del robot
mover_robot()

# Ejecutar la ventana
root.mainloop()
