from utils import morphological_reconstruction, read_image
from config import IMAGES_PATH
import cv2
import numpy as np


def generate_image_G():
    # leemos las imagenes
    image_F = read_image(f"{IMAGES_PATH}/image_F.bmp")
    image_F_bool = image_F > 0
    
    image_C = read_image(f"{IMAGES_PATH}/image_C.bmp")
    image_C_bool = image_C > 0
    
    # la imagen G se obtiene mediante la operación XOR entre C y F
    image_G = image_C_bool ^ image_F_bool
    
    cv2.imwrite(f"{IMAGES_PATH}/image_G.bmp", image_G.astype(np.uint8) * 255)