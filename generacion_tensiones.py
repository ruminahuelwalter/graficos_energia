# Grafico tensiones trifasicas
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.02, 1000)  # 1 ciclo de 50 Hz
V_R = 100 * np.sin(2 * np.pi * 50 * t)
V_S = 100 * np.sin(2 * np.pi * 50 * t - np.deg2rad(120))
V_T = 100 * np.sin(2 * np.pi * 50 * t - np.deg2rad(240))

plt.plot(t, V_R, 'r', label='Fase R')
plt.plot(t, V_S, 'b', label='Fase S')
plt.plot(t, V_T, 'g', label='Fase T')
plt.legend()
plt.grid()
plt.title("Tensiones trifásicas")
plt.show()