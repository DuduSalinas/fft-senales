import numpy as np
import matplotlib.pyplot as plt

# =========================
# Parámetros generales
# =========================
fs = 1000            # Frecuencia de muestreo [Hz]
T = 1.0              # Duración [s]
N = int(fs * T)      # Muestras totales
t = np.arange(N) / fs

def fft_mag_phase(x, fs):
    N = len(x)
    X = np.fft.fft(x)
    f = np.fft.fftfreq(N, d=1/fs)
    # Ordenar para espectro centrado (opcional)
    X_shift = np.fft.fftshift(X)
    f_shift = np.fft.fftshift(f)
    mag = np.abs(X_shift)
    phase = np.angle(X_shift)
    return f_shift, mag, phase

def plot_time_and_freq(t, x, f, mag, phase, title_base, save_prefix):
    plt.figure(figsize=(12, 8))
    plt.subplot(2,2,1)
    plt.plot(t, x, lw=1.5)
    plt.title(f"{title_base} - Tiempo")
    plt.xlabel("Tiempo [s]"); plt.ylabel("Amplitud"); plt.grid(True)

    plt.subplot(2,2,2)
    plt.plot(f, mag, lw=1.5)
    plt.title(f"{title_base} - Magnitud")
    plt.xlabel("Frecuencia [Hz]"); plt.ylabel("|X(f)|"); plt.grid(True)

    plt.subplot(2,2,4)
    plt.plot(f, phase, lw=1.0)
    plt.title(f"{title_base} - Fase")
    plt.xlabel("Frecuencia [Hz]"); plt.ylabel("∠X(f) [rad]"); plt.grid(True)

    plt.tight_layout()
    plt.savefig(f"figures/{save_prefix}.png", dpi=150)
    plt.show()

# =========================
# 1) Señal senoidal
# =========================
f0 = 50
A = 1.0
x_sine = A * np.sin(2*np.pi*f0*t)
f_sine, mag_sine, phase_sine = fft_mag_phase(x_sine, fs)
plot_time_and_freq(t, x_sine, f_sine, mag_sine, phase_sine, "Senoidal 50 Hz", "senoidal_50Hz")

# =========================
# 2) Escalón (u[n])
# =========================
# En tiempo continuo, el escalón no es absolutamente integrable; discretamente lo truncamos.
x_step = np.ones_like(t)
f_step, mag_step, phase_step = fft_mag_phase(x_step, fs)
plot_time_and_freq(t, x_step, f_step, mag_step, phase_step, "Escalón truncado", "escalon_truncado")

# =========================
# 3) Pulso rectangular
# =========================
# Pulso de ancho 0.2 s centrado al inicio (0 <= t < 0.2)
width = 0.2
x_rect = np.where((t >= 0.0) & (t < width), 1.0, 0.0)
f_rect, mag_rect, phase_rect = fft_mag_phase(x_rect, fs)
plot_time_and_freq(t, x_rect, f_rect, mag_rect, phase_rect, "Pulso rectangular (0.2 s)", "pulso_rectangular")

# =========================
# Propiedad de linealidad: a*x1 + b*x2 -> a*X1 + b*X2
# =========================
a, b = 0.7, 0.3
x_lin = a*x_sine + b*x_rect
f_lin, mag_lin, phase_lin = fft_mag_phase(x_lin, fs)
plot_time_and_freq(t, x_lin, f_lin, mag_lin, phase_lin, "Linealidad: 0.7*seno + 0.3*pulso", "linealidad")

# =========================
# Propiedad de desplazamiento en el tiempo: x(t - t0) -> X(f) * e^{-j2π f t0}
# =========================
t0 = 0.1
# Desplazamiento discreto: desplazar índices
shift_samples = int(t0 * fs)
x_rect_shift = np.roll(x_rect, shift_samples)
f_shifted, mag_shifted, phase_shifted = fft_mag_phase(x_rect_shift, fs)
plot_time_and_freq(t, x_rect_shift, f_shifted, mag_shifted, phase_shifted, "Pulso desplazado 0.1 s", "pulso_desplazado")

# =========================
# Escalamiento en el tiempo (equivale a escalamiento en frecuencia)
# x(a t) <-> (1/|a|) X(f / a)
# =========================
# A nivel discreto, simular 'comprimir' la señal duplicando frecuencia efectiva
f0_2 = 100
x_sine_fast = A * np.sin(2*np.pi*f0_2*t)
f_fast, mag_fast, phase_fast = fft_mag_phase(x_sine_fast, fs)
plot_time_and_freq(t, x_sine_fast, f_fast, mag_fast, phase_fast, "Senoidal 100 Hz (escalado en tiempo)", "senoidal_100Hz")

# =========================
# Comparación de dominio de frecuencia: ventana y padding (mejora visual)
# =========================
# Ventana Hamming para el seno de 50 Hz
w = np.hamming(N)
x_sine_win = x_sine * w
f_win, mag_win, phase_win = fft_mag_phase(x_sine_win, fs)
plot_time_and_freq(t, x_sine_win, f_win, mag_win, phase_win, "Senoidal 50 Hz con ventana Hamming", "senoidal_ventana")

# Zero-padding para mayor resolución en frecuencia
pad_factor = 4
X_pad = np.fft.fft(x_sine, n=N*pad_factor)
f_pad = np.fft.fftfreq(N*pad_factor, d=1/fs)
X_pad_shift = np.fft.fftshift(X_pad)
f_pad_shift = np.fft.fftshift(f_pad)
mag_pad = np.abs(X_pad_shift)
phase_pad = np.angle(X_pad_shift)

plt.figure(figsize=(10,6))
plt.plot(f_sine, mag_sine, label="Sin padding", alpha=0.7)
plt.plot(f_pad_shift, mag_pad, label=f"Padding x{pad_factor}", alpha=0.7)
plt.title("Comparación de magnitud (seno 50 Hz) con/ sin padding")
plt.xlabel("Frecuencia [Hz]"); plt.ylabel("|X(f)|"); plt.grid(True); plt.legend()
plt.tight_layout()
plt.savefig("figures/senoidal_padding.png", dpi=150)
plt.show()