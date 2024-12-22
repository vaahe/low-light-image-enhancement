import cv2
import os
from enhancement.core import enhance_image

def test_enhance_image():
    for filename in os.listdir("data/input"):
        input_path = os.path.join("data/input", filename)
        image = cv2.imread(input_path)
        enhanced_image = enhance_image(image)
        
        assert enhanced_image is not None
        assert enhanced_image.shape == image.shape
        assert enhanced_image.dtype == image