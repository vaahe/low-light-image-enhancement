import cv2
import numpy as np

def read_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def preprocess_image(image):
    """ Apply noise reduction """
    return cv2.bilateralFilter(image, 9, 3, 3)

def adjust_brightness_contrast(image):
    """ Adjust brightness and contrast """
    gamma = 2.0
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def enhance_details(image):
    """ Enhances details using unsharp masking """
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
    return sharpened

def adjust_color_balance(image):
    """ Adjust color balance by applying white balance correction """
    result = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(result)
    l = cv2.equalizeHist(l)
    result = cv2.merge((l, a, b))
    return cv2.cvtColor(result, cv2.COLOR_LAB2BGR) 

def is_low_light(image):
    """ Check if image is low light using histogram """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist = hist / hist.sum()
    low_light_percentage = np.sum(hist[:50]) * 100 
    low_light_threshold = 40
    return low_light_percentage > low_light_threshold