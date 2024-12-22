import matplotlib.pyplot as plt

def visualize_images(original_image, processed_image, title_original='Original Image', title_processed='Processed Image'):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    axes[0].imshow(original_image, cmap='gray')
    axes[0].set_title(title_original)
    axes[0].axis('off')
    
    axes[1].imshow(processed_image, cmap='gray')
    axes[1].set_title(title_processed)
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()