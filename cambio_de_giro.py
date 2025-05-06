import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# Configuración
f = 50  # Frecuencia (Hz)
Vmax = 100  # Voltaje máximo (V)
t = np.linspace(0, 1/f, 100)  # 1 ciclo (20 ms)

# Funciones para las ondas
def onda_R(t):
    return Vmax * np.sin(2 * np.pi * f * t)

def onda_S(t):
    return Vmax * np.sin(2 * np.pi * f * t - np.deg2rad(240))  # Ahora S ocupa el lugar de T

def onda_T(t):
    return Vmax * np.sin(2 * np.pi * f * t - np.deg2rad(120))  # T ocupa el lugar de S
# Crear figura
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico de ondas
ax1.set_xlim(0, 1/f)
ax1.set_ylim(-Vmax*1.2, Vmax*1.2)
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Voltaje (V)')
ax1.grid(True)
ax1.set_title('Ondas Trifásicas')

line_R, = ax1.plot([], [], 'r-', label='Fase R')
line_S, = ax1.plot([], [], 'b-', label='Fase S')
line_T, = ax1.plot([], [], 'g-', label='Fase T')
ax1.legend()

# Gráfico polar (campo magnético)
ax2 = plt.subplot(122, polar=True)
ax2.set_title('Campo Magnético Rotante')
ax2.set_theta_zero_location('E')
B_arrow = ax2.quiver(0, 0, 0, 0, color='r', scale=100)

# Inicialización
def init():
    line_R.set_data([], [])
    line_S.set_data([], [])
    line_T.set_data([], [])
    return line_R, line_S, line_T, B_arrow

# Animación
def update(frame):
    # Actualizar ondas
    current_t = t[:frame]
    line_R.set_data(current_t, onda_R(current_t))
    line_S.set_data(current_t, onda_S(current_t))
    line_T.set_data(current_t, onda_T(current_t))
    
    # Calcular campo magnético (suma fasorial)
    B_R = onda_R(t[frame]) * np.exp(1j * 0)
    B_S = onda_S(t[frame]) * np.exp(1j * np.deg2rad(120))
    B_T = onda_T(t[frame]) * np.exp(1j * np.deg2rad(240))
    B_total = B_R + B_S + B_T
    
    # Actualizar flecha del campo
    B_arrow.set_UVC(np.real(B_total), np.imag(B_total))
    
    return line_R, line_S, line_T, B_arrow

# Ejecutar animación
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=50)
plt.tight_layout()
plt.show()