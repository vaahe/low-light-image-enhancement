import os

from enhancement.core import enhance_image
from enhancement.preprocess import read_image
from enhancement.postprocess import save_image
from utils.metrics import calculate_psnr, calculate_ssim

def main():
    input_dir = "data/input"
    output_dir = "data/output"
    psnr_dir = "data/psnr"

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        image = read_image(input_path)
        enhanced_image = enhance_image(image)
        save_image(enhanced_image, output_path)

    for filename in os.listdir(psnr_dir):
        psnr_path = os.path.join(psnr_dir, filename)
        output_path = os.path.join(output_dir, filename)

        if os.path.exists(output_path):
            psnr_image = read_image(psnr_path)
            output_image = read_image(output_path)
            psnr_value = calculate_psnr(psnr_image, output_image)
            print(f"PSNR for {filename}: {psnr_value}")
            print(f"SSIM for {filename}: {calculate_ssim(psnr_image, output_image)}")
        else:
            print(f"Output image for {filename} not found.")

if __name__ == "__main__":
    main()