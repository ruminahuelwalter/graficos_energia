import numpy as np  
import matplotlib.pyplot as plt  

# Parámetros  
t = np.linspace(0, 1/50, 100)  # 1 ciclo de 50 Hz  

# Secuencia R-S-T (horario)  
V_R = np.sin(2 * np.pi * 50 * t)  
V_S = np.sin(2 * np.pi * 50 * t - 2*np.pi/3)  
V_T = np.sin(2 * np.pi * 50 * t - 4*np.pi/3)  

plt.plot(t, V_R, 'r', label='R')  
plt.plot(t, V_S, 'b', label='S')  
plt.plot(t, V_T, 'g', label='T')  
plt.legend()  
plt.title("Secuencia R-S-T (Giro horario)")  
plt.show()  