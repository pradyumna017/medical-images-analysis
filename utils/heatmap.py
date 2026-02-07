import numpy as np
import cv2

def generate_heatmap(image):
    h, w = image.shape
    heatmap = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(heatmap, (w//2, h//2), 80, 255, -1)
    return heatmap
