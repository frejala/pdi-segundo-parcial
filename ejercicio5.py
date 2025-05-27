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
    reconstructed_background = morphological_reconstruction(marker, inverted_image_C_bool)
    
    # invertimos la imagen para obtener el fondo relleno
    C_filled = ~reconstructed_background
    
    # cv2.imwrite("filled.bmp", C_filled.astype(np.uint8) * 255)
    
    # aplicamos xor para obtener los agujeros
    holes = C_filled ^ image_C
    
    # invertimos los agujeros para trabajar con ellos
    holes_inv = ~holes
    
    # cv2.imwrite("holes.bmp", holes_inv.astype(np.uint8) * 255)
    
    # creamos un marcador que contiene los bordes de los agujeros
    holes_marker = np.zeros_like(holes_inv, dtype=bool)
    holes_marker[0, :] = holes_inv[0, :]
    holes_marker[-1, :] = holes_inv[-1, :]
    holes_marker[:, 0] = holes_inv[:, 0]
    holes_marker[:, -1] = holes_inv[:, -1]
    
    # reconstruimos la imagen de agujeros
    reconstructed_holes = morphological_reconstruction(holes_marker, holes_inv)
    
    # invertimos
    reconstructed_holes_inv = ~reconstructed_holes
    
    # cv2.imwrite(f"recons.bmp", reconstructed_holes_inv.astype(np.uint8) * 255)
    
    # aplicamos un and para obtener la imagen E
    imgae_E = holes_inv & reconstructed_holes_inv

    image_E = imgae_E.astype(np.uint8) * 255
    cv2.imwrite(f"{IMAGES_PATH}/image_E.bmp", image_E)