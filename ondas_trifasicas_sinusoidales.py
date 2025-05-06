import numpy as np
print(np.__version__)  # Debería mostrar 2.2.5
import matplotlib.pyplot as plt

# campo_magnetico_rotante
# cambio_de_giro


# Parámetros
f = 50  # Frecuencia (Hz)
Vmax = 100  # Voltaje máximo (V)
t = np.linspace(0, 1/f, 1000)  # 1 ciclo (20 ms)

# Ondas trifásicas
V_R = Vmax * np.sin(2 * np.pi * f * t)
V_S = Vmax * np.sin(2 * np.pi * f * t - np.deg2rad(120))
V_T = Vmax * np.sin(2 * np.pi * f * t - np.deg2rad(240))

# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(t, V_R, label='Fase R', color='red')
plt.plot(t, V_S, label='Fase S', color='blue')
plt.plot(t, V_T, label='Fase T', color='green')
plt.title('Ondas Trifásicas (Secuencia R-S-T)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid()
plt.legend()
plt.show()