# Procesamiento Digital de Imágenes

### Integrantes
Fabrizio Rejala - 5775001 \
Hadi Faour - 8116060

| Ejercicio | Genera | Operaciones clave |
|-----------|--------|-------------------|
| **A** | Células completas (sin las que tocan el borde) | Reconstrucción + AND/NOT |
| **B** | Agujeros (citoplasmas) | Reconstrucción + AND/NOT |
| **C** | Células con agujero (Tipos 2-3-4) | Reconstrucción sobre máscara |
| **D** | Células sin agujero (Tipo 1) | AND |

---

## Estructura del proyecto
```text
.
├── images/                 # BMP originales y resultados
│   ├── original.bmp
│   ├── image_A.bmp
│   ├── image_B.bmp
│   ├── image_C.bmp
│   └── image_D.bmp
│
├── config.py               # Ruta base de 'images'
├── utils.py                # read_image() y morphological_reconstruction()
│
├── ejercicio1.py           # Genera image_A.bmp
├── ejercicio2.py           # Genera image_B.bmp
├── ejercicio3.py           # Genera image_C.bmp
├── ejercicio4.py           # Genera image_D.bmp
│
├── main.py                 # Ejecuta los cuatro ejercicios en cadena
├── requirements.txt        # Dependencias (OpenCV, NumPy, SciPy)
└── README.md               # Este archivo
```

---

## Instalación rápida

```bash
# Crea y activa un entorno virtual (opcional)
python -m venv .venv
# En Linux y MacOS
source .venv/bin/activate
# En Windows
.venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
# Ejecuta todos los ejercicios
python main.py
```

