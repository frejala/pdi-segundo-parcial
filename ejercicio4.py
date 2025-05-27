from utils import morphological_reconstruction, read_image
from config import IMAGES_PATH
import cv2
import numpy as np


def generate_image_D():
    image_C = read_image(f"{IMAGES_PATH}/image_C.bmp")
    image_A = read_image(f"{IMAGES_PATH}/image_A.bmp")

    # Invertir la imagen C (tienen los citoplasmas)
    inverted_image_C = ~image_C > 0
    
    # AND de la imagen A con la imagen C invertida
    image_D = inverted_image_C & (image_A > 0)
    
    image_D = image_D.astype(np.uint8) * 255
    cv2.imwrite(f"{IMAGES_PATH}/image_D.bmp", image_D)