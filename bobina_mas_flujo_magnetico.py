import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle, Arrow

# Configuración
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()

# Campo magnético (representado por flechas horizontales)
B_direction = 1  # 1: derecha, -1: izquierda
for y in np.linspace(-1.5, 1.5, 10):
    ax.add_patch(Arrow(-1.5, y, 3, 0, width=0.05, color='blue', alpha=0.3))

# Bobina (inicialmente vertical)
bobina, = ax.plot([], [], 'ro-', lw=3, markersize=10)
flujo_text = ax.text(0.5, 1.5, "", fontsize=12, color='green')

# Área de la bobina (para calcular Φ_B)
A = 1.0  # Área normalizada
B = 1.0  # Campo magnético normalizado

voltaje_text = ax.text(0.5, 1.3, "", fontsize=12, color='orange')

def update(frame):
    angle = np.radians(frame)
    # Actualizar posición de la bobina
    x = np.array([-np.sin(angle), np.sin(angle)])
    y = np.array([-np.cos(angle), np.cos(angle)])
    bobina.set_data(x, y)
    
    # Calcular flujo magnético Φ_B = B · A · cos(θ)
    phi_B = B * A * np.cos(angle)
    
    # Mostrar flujo en el gráfico
    flujo_text.set_text(f"Flujo Φ_B = {phi_B:.2f}")
    
    # Cambiar color si el flujo es positivo/negativo
    bobina.set_color('red' if phi_B >= 0 else 'purple')

    epsilon = -B * A * np.sin(angle)  # ε = -dΦ_B/dt
    voltaje_text.set_text(f"Voltaje ε = {epsilon:.2f}")
  
    return bobina, flujo_text, voltaje_text


ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
plt.title("Bobina girando en campo magnético (azul)")
plt.xlabel("Flujo Φ_B = B · A · cos(θ)")
plt.show()

