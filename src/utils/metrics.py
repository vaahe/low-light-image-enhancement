import math
import numpy as np
import cv2

from skimage.metrics import structural_similarity as ssim

def calculate_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def calculate_ssim(original, processed):
    gray_original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    gray_processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(gray_original, gray_processed, full=True)
    return score