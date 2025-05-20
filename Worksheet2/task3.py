import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
# Load the original image
original_image = cv2.imread( 'Pic1.jpeg', cv2.IMREAD_GRAYSCALE)
# Check if the image was loaded successfully
if original_image is None:
    print("Error: Unable to load the original image. Please check the file path and image format.")
else:
# Create a reconstructed version of the original image (e.g., using some image processing technique)
# Here, we'll simply add some random noise to the original image to simulate reconstruction
    reconstructed_image = original_image + np.random.normal(0, 20, original_image.shape)
# Ensure pixel values are within valid range (0 to 255)
    reconstructed_image = np.clip(reconstructed_image, 0, 255).astype(np.uint8)
# Calculate Mean Squared Error (MSE)
    mse = np.mean((original_image - reconstructed_image) ** 2)
# Calculate Peak Signal-to-Noise Ratio (PSNR)
    psnr = cv2.PSNR(original_image, reconstructed_image)
# Calculate Structural Similarity Index (SSIM)
    ssim_index, _ = ssim(original_image, reconstructed_image, full=True)
# Visualize original and reconstructed images along with fidelity metrics
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(reconstructed_image, cmap='gray')
plt.title('Reconstructed Image')
plt.axis('off')
plt.suptitle(f'Fidelity Metrics:\nMSE: {mse:.2f}, PSNR: {psnr:.2f} dB, SSIM: {ssim_index:.2f}')
plt.show()