# Portada
Simulación y análisis de señales con la Transformada de Fourier
Actividad formativa 2 — Cristian González Salinas

# Objetivo e instrumentos
Analizar señales en tiempo y frecuencia con FFT y STFT, comparando propiedades y ventanas.
Herramientas: MATLAB (Online/Escritorio), Python (NumPy/SciPy/Matplotlib/Jupyter), GitHub.

# Conceptos clave
- Dominio del tiempo y de la frecuencia.
- FFT: magnitud y fase; resolución Δf = fs/N.
- STFT: espectrograma, ventana y solapamiento.
- Propiedades: linealidad, desplazamiento, escalamiento.

# Señales y parámetros
Senoidal (50/100 Hz), escalón truncado, pulso rectangular (0.2 s).
fs = 1000 Hz, T = 1 s, N = 1000.

# FFT: resultados
Picos en ±f0 para senoidales. Pulso → espectro tipo sinc. Escalón → energía en bajas frecuencias.

# Propiedades demostradas
Linealidad: suma en tiempo ↔ suma en frecuencia.
Desplazamiento: altera fase, no magnitud.
Escalamiento: comprimir en tiempo ↔ expandir en frecuencia.

# Ventanas y padding
Hamming, Hann, Blackman: reducen leakage.
Zero-padding: mayor densidad de muestreo en frecuencia (no aumenta resolución real).

# STFT y espectrogramas
Muestra cómo cambian las frecuencias en el tiempo. Ventana: balance tiempo/frecuencia.

# Conclusiones
La transformada de Fourier revela componentes frecuenciales y su evolución temporal, útil en diagnóstico y comunicaciones.¡