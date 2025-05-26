import cv2
import numpy as np


image_path = "5ab3_0Artificial.bmp"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


def morphological_reconstruction(marker, mask):
    se = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    rec = marker.copy()
    
    while True:
        dil = cv2.dilate(rec, se)
        rec_next = cv2.bitwise_and(dil, mask)
        if np.array_equal(rec_next, rec):
            break
        rec = rec_next
    return rec

