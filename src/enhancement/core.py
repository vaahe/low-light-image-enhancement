from .postprocess import postprocess_image
from .preprocess import enhance_details, preprocess_image, adjust_color_balance, adjust_brightness_contrast, is_low_light

def enhance_image(image):
    if not is_low_light(image):
        return image
    
    preprocessed = preprocess_image(image)
    brightness_adjusted = adjust_brightness_contrast(preprocessed)
    details_enhanced = enhance_details(brightness_adjusted)
    color_balanced = adjust_color_balance(details_enhanced)
    final_image = postprocess_image(color_balanced)
    return final_image
