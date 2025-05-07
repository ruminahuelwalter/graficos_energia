from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt  

def update(frame):
    ax.clear()
    # Dibujar bobina en ángulo 'frame'
    angle = frame * np.pi / 180
    x = np.cos(angle)
    y = np.sin(angle)
    ax.plot([-x, x], [-y, y], 'o-', linewidth=3)  # Bobina
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'Bobina en θ = {frame}°')

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 10), interval=100)
plt.show()