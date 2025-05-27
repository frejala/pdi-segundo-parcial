from utils import morphological_reconstruction, read_image
from config import IMAGES_PATH
from scipy.ndimage import binary_dilation
import cv2
import numpy as np

def generate_image_F():
    # Leer las imágenes necesarias
    image_C = read_image(f"{IMAGES_PATH}/image_C.bmp")
    image_C_bool = image_C > 0
    image_E = read_image(f"{IMAGES_PATH}/image_E.bmp")
    image_E_bool = image_E > 0
    
    # se dilata E
    dilatated_E = binary_dilation(image_E_bool, iterations=4)
    
    # cv2.imwrite(f"dilatated_E.bmp", dilatated_E.astype(np.uint8) * 255)
    
    # la imagen F se obtiene mediante la reconstrucción morfológica
    # de la imagen dilatada E con la imagen C como marcador
    image_F = morphological_reconstruction(dilatated_E, image_C_bool)
    
    cv2.imwrite(f"{IMAGES_PATH}/image_F.bmp", image_F.astype(np.uint8) * 255)