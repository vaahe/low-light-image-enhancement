import cv2

def save_image(image, output_path):
    cv2.imwrite(output_path, image)

def postprocess_image(image):
    guided = cv2.ximgproc.guidedFilter(image, image, 8, 10)
    return guided