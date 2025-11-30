📊 Simulación y Análisis de Señales con Fourier (FFT/STFT) en MATLAB y Python

🎯 Objetivo

Analizar señales en tiempo y frecuencia aplicando FFT y STFT. Demostrar propiedades: linealidad, desplazamiento temporal y escalamiento, y comparar ventanas.

---

📁 Estructura del Proyecto

```
proyecto-fft-stft/
├── 📁 src/
│   ├── 📁 python/
│   │   ├── `analisis_fft.py` - Script Python (FFT, ventanas, padding, propiedades)
│   │   └── `analisis_fft_stft.ipynb` - Notebook Jupyter (FFT + STFT)
│   └── 📁 matlab/
│       ├── `analisis_fft.m` - Script MATLAB (FFT y propiedades)
│       └── `analisis_stft.m` - Script MATLAB (STFT y ventanas)
├── 📁 figures/ - Gráficas generadas automáticamente
└── 📁 docs/
    ├── `presentacion_fft.pptx` - Plantilla PowerPoint editable
    ├── `canva_texto_base.md` - Bloques de texto para Canva
    └── `informe_fft.md` - Guía del informe técnico
```

---

⚙️ Requisitos

· Python 3.10+ con las librerías: NumPy, SciPy, Matplotlib, Jupyter
· MATLAB (Online o versión de escritorio)

---

🐍 Instalación para Python

```bash
pip install -r requirements.txt
```

---

🚀 Ejecución

Para scripts de Python:

```bash
cd src/python
python analisis_fft.py
```

Para Jupyter Notebook:

```bash
jupyter notebook analisis_fft_stft.ipynb
```

Para MATLAB:

· Ejecutar los scripts .m desde el entorno de MATLAB
