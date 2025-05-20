import numpy as np
import cv2

def compute_psnr_y_channel(original_img, compressed_img):

    # Convert to YCrCb and extracting y-channel
    y_original = cv2.cvtColor(original_img, cv2.COLOR_BGR2YCrCb)[:, :, 0]
    y_compressed = cv2.cvtColor(compressed_img, cv2.COLOR_BGR2YCrCb)[:, :, 0]
    
    # Compute Mean Squared Error (MSE)
    mse = np.mean((y_original.astype(np.float64) - y_compressed.astype(np.float64)) ** 2)
    
    if mse == 0:
        return float('inf')  # No distortion
    
    # Maximum pixel value for 8-bit image
    R = 255.0
    
    # Compute PSNR
    psnr = 10 * np.log10((R ** 2) / mse)
    
    return psnr