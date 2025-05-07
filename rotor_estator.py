import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle, Rectangle

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()

# Configuración del rotor (imán giratorio)
rotor = Circle((0, 0), 0.5, color='red', alpha=0.5)
polo_norte = Rectangle((-0.1, 0.4), 0.2, 0.1, color='blue')  # Polo Norte (azul)
polo_sur = Rectangle((-0.1, -0.5), 0.2, 0.1, color='green')  # Polo Sur (verde)
ax.add_patch(rotor)
ax.add_patch(polo_norte)
ax.add_patch(polo_sur)

# Bobinas fijas (estator)
bobina1, = ax.plot([1.5, 1.5], [-0.2, 0.2], 'ko-', lw=3)  # Bobina derecha
bobina2, = ax.plot([-1.5, -1.5], [-0.2, 0.2], 'ko-', lw=3)  # Bobina izquierda
bobina3, = ax.plot([-0.2, 0.2], [1.5, 1.5], 'ko-', lw=3)  # Bobina superior
bobina4, = ax.plot([-0.2, 0.2], [-1.5, -1.5], 'ko-', lw=3)  # Bobina inferior

# Texto para el flujo
flujo_text = ax.text(0, 1.8, "", fontsize=12, ha='center')

def update(frame):
    angle = np.radians(frame)
    # Rotar el imán (rotor)
    polo_norte.set_xy([-0.1 * np.cos(angle) - 0.1 * np.sin(angle), 
                      0.4 * np.cos(angle) - 0.1 * np.sin(angle)])
    polo_sur.set_xy([-0.1 * np.cos(angle) + 0.1 * np.sin(angle), 
                    -0.5 * np.cos(angle) + 0.1 * np.sin(angle)])
    
    # Calcular flujo en una bobina (ejemplo: bobina derecha)
    flujo = np.cos(angle)  # Flujo máximo cuando el polo norte apunta hacia la bobina
    flujo_text.set_text(f"Flujo Φ_B = {flujo:.2f}")
    
    return polo_norte, polo_sur, flujo_text

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
plt.title("Generador: Rotor (imán) girando y Estator (bobinas fijas)")
plt.show()