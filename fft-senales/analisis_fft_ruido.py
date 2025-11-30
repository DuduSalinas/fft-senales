import numpy as np
import matplotlib.pyplot as plt
import os

⋕ Crear carpeta para guardar imagenes 
if not os.path.exists("figures"):
    os.makedirs("figures")

⋕ Parametros generales
fs = 1000       · Frecuencia de muestra [Hz]
T = 1.0         ⋕ Duracion [s]
N = int(fs * T) ⋕ Numero de muestras
t = np.arange(N) / fs

⋕ =============================
⋕ 1) Senal compuesta +  ruido
⋕ =============================
f1, f2 = 50, 120    ⋕ dos frecuencias
signal_clean = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)
noise = 0.3*np.random.randn(N)
signal_noisy = signal_clean + noise

⋕ FFT de la senal con ruido
X = np.fft.fft(signal_noisy)
f = np.fft.fftfreq(N, d=1/fs)
X_shift = np.fft.fftshift(x)
f_shift = np.fft.fftshift(f)

⋕ Graficas
plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.plot(t, signal_noisy)
plt.title("Senal compuesta con ruido - Tiempo")
plt.xlabel("Tiempo [s]"); plt.ylabel("Amplitud"); plt.grid(True)

plt.subplot(2,2,2)
plt.plot(f_shift, np,abs(X_shift))
plt.title("FFT de señal con ruido - Magnitud")
plt.xlabel("Frecuencia [Hz]"); plt.ylabel("|X(f)|"); plt.grid(True)

plt.tight_layout()
plt.savefig("figures/senal_ruido_fft.png", dpi=150)
plt.show()

⋕ ============================
⋕ 2) Filtrado eb frecuencia
⋕ ============================
⋕ creamos un filtro pasa-banda para conservar solo 40-130 Hz
mask = (np.abs(f) > 40) & (np.abs(f) < 130)
X_filtered = x * mask
signal_filtered = np.fft.ifft(X_filtered)

⋕FFT de la señal filtrada
Xf_shift = np.fft.fftshift(X_filtered)

plt.figure(figsize0(12,8))
plt.subplot(2,2,1)
plt.plot(t, signal_filtered.real)
plt.title("señal filtrada (40-130 Hz) - Tiempo")
plt.xlabel("tiempo [s]"); plt.ylabel("Amplitud"); plt.grid(True)

plt.subplot(2,2,2)
plt.plot(f_shift, np.abs(Xf_shift))
plt.title("FFT de señal filtrada - Magnitud")
plt.xlabel("Frecuencia [Hz]"); plt.ylabel("|X(f)|"); plt.grid(True)

plt.tight_layout()
plt.savefig("figures/senal_filtrada_fft.png", dpi=150)
plt.show()