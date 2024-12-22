import pytest
import numpy as np

from src.utils.metrics import calculate_psnr, calculate_ssim
from src.utils.visualization import visualize_images

def test_calculate_psnr():
    img1 = np.ones((256, 256), dtype=np.uint8) * 255
    img2 = np.ones((256, 256), dtype=np.uint8) * 128
    psnr = calculate_psnr(img1, img2)
    assert psnr > 0

def test_calculate_ssim():
    img1 = np.ones((256, 256), dtype=np.uint8) * 255
    img2 = np.ones((256, 256), dtype=np.uint8) * 128
    ssim = calculate_ssim(img1, img2)
    assert 0 <= ssim <= 1

def test_visualize_images():
    img1 = np.ones((256, 256), dtype=np.uint8) * 255
    img2 = np.ones((256, 256), dtype=np.uint8) * 128
    
    try:
        visualize_images([img1, img2])
    except Exception as e:
        pytest.fail(f"visualize_images raised an exception: {e}")