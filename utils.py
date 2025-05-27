import numpy as np
from scipy.ndimage import binary_dilation
import cv2


def read_image(path, grayscale=True):
    """
    Lee una imagen desde la ruta especificada.
    
    :param path: Ruta de la imagen.
    :return: Imagen leída.
    """
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def morphological_reconstruction(marker, mask):
    """
    Realiza la reconstrucción morfológica de una imagen utilizando un marcador y una máscara.
    
    :param marker: Imagen marcador (debe ser un array booleano).
    :param mask: Imagen máscara (debe ser un array booleano).
    :return: Imagen reconstruida.
    """
    if marker.shape != mask.shape:
        raise ValueError("Las dimensiones de marker y mask deben ser iguales.")

    reconstructed = marker.copy()
    
    while True:
        previous = reconstructed.copy()
        dilated = binary_dilation(reconstructed)
        reconstructed = dilated & mask
        if np.array_equal(reconstructed, previous):
            break
    
    return reconstructed