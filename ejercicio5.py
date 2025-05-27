from utils import morphological_reconstruction, read_image
from config import IMAGES_PATH
import cv2
import numpy as np

def generate_image_E():
    # Leer las imágenes necesarias
    image_C = read_image(f"{IMAGES_PATH}/image_C.bmp")
    image_C = image_C > 0 
    inverted_image_C_bool = ~image_C > 0
    
    # se crea el marcador desde los bordes
    marker = np.zeros_like(inverted_image_C_bool, dtype=bool)
    marker[0, :] = inverted_image_C_bool[0, :]
    marker[-1, :] = inverted_image_C_bool[-1, :]
    marker[:, 0] = inverted_image_C_bool[:, 0]
    marker[:, -1] = inverted_image_C_bool[:, -1]
    
    # se rellena el fondo
    reconstruction_inverted = ~morphological_reconstruction(marker, inverted_image_C_bool)
    
    # aplicamos xor para obtener los agujeros e invertimos
    holes = ~(reconstruction_inverted ^ image_C)
        
    # creamos un marcador que contiene los bordes de los agujeros
    holes_marker = np.zeros_like(holes, dtype=bool)
    holes_marker[0, :] = holes[0, :]
    holes_marker[-1, :] = holes[-1, :]
    holes_marker[:, 0] = holes[:, 0]
    holes_marker[:, -1] = holes[:, -1]
    
    # reconstruimos la imagen de agujeros
    reconstructed_holes = ~morphological_reconstruction(holes_marker, holes)
        
    # aplicamos un and para obtener la imagen E
    imgae_E = holes & reconstructed_holes

    image_E = imgae_E.astype(np.uint8) * 255
    cv2.imwrite(f"{IMAGES_PATH}/image_E.bmp", image_E)