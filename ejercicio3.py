from utils import morphological_reconstruction, read_image
from config import IMAGES_PATH
import cv2
import numpy as np

def generate_image_C():
    image_A = read_image(f"{IMAGES_PATH}/image_A.bmp")
    image_B = read_image(f"{IMAGES_PATH}/image_B.bmp")
    
    # Se usa la imagen B como marcador
    marker = image_B > 0
    
    # Se usa la imagen A como máscara (se invierte para la reconstrucción)
    mask = ~image_A > 0
    
    # Realiza la reconstrucción morfológica
    image_C = morphological_reconstruction(marker, mask)
    image_C = image_C.astype(np.uint8) * 255
    
    cv2.imwrite(f"{IMAGES_PATH}/image_C.bmp", image_C)
    
    
               