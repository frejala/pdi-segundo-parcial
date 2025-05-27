from utils import morphological_reconstruction, read_image
from config import IMAGES_PATH
import cv2
import numpy as np


def generate_image_A():
    image = read_image(f"{IMAGES_PATH}/original.bmp")

    _, binary_image = cv2.threshold(~image, 127, 255, cv2.THRESH_BINARY)
    binary_image_bool = binary_image > 0

    marker = np.zeros_like(binary_image_bool, dtype=bool)
    marker[0, :] = binary_image_bool[0, :]
    marker[-1, :] = binary_image_bool[-1, :]
    marker[:, 0] = binary_image_bool[:, 0]
    marker[:, -1] = binary_image_bool[:, -1]

    border_objects = morphological_reconstruction(marker, binary_image_bool)

    image_A = binary_image_bool & (~border_objects)
    image_A = image_A.astype(np.uint8) * 255

    cv2.imwrite(f"{IMAGES_PATH}/image_A.bmp", image_A)
