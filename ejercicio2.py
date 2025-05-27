from utils import morphological_reconstruction, read_image
from config import IMAGES_PATH
import cv2
import numpy as np


def generate_image_B():
    image = read_image(f"{IMAGES_PATH}/image_A.bmp")

    # obtenemos la imagen binaria e invertimos los colores
    _, binary_image = cv2.threshold(~image, 127, 255, cv2.THRESH_BINARY)
    binary_image_bool = binary_image > 0                    
    
    # creamos el marcador
    marker = np.zeros_like(binary_image_bool, dtype=bool)
    marker[0,  :] = binary_image_bool[0,  :]
    marker[-1, :] = binary_image_bool[-1, :]
    marker[:, 0]  = binary_image_bool[:, 0]
    marker[:, -1] = binary_image_bool[:, -1]

    # realizamos la reconstruccion morfologica
    exterior = morphological_reconstruction(marker, binary_image_bool)

    # obtenemos la imagen B
    # AND -> Nos quedamos con todo lo blanco
    image_B = binary_image_bool & (~exterior)
    image_B = image_B.astype(np.uint8) * 255
    
    cv2.imwrite(f"{IMAGES_PATH}/image_B.bmp", image_B)