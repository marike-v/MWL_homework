import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load images
original_lena = Image.open('lena.png').convert('RGB')
original_landscape = Image.open('landscape.png').convert('RGB')
#converting images to np arrays so that psnr can be calculated
lena_np=np.array(original_lena)
landscape_np=np.array(original_landscape)


images= {'Lena': lena_np, 'Landscape': landscape_np}
qualities = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def compute_psnr_y_channel(original_img, compressed_img):

    # Convert to YCrCb and extracting y-channel
    y_original = cv2.cvtColor(original_img, cv2.COLOR_BGR2YCrCb)[:, :, 0]
    y_compressed = cv2.cvtColor(compressed_img, cv2.COLOR_BGR2YCrCb)[:, :, 0]
    
    # Compute Mse
    mse = np.mean((y_original.astype(np.float64) - y_compressed.astype(np.float64)) ** 2)
    
    if mse == 0:
        return float('inf')  # No distortion
    
    # Maximum pixel value for 8-bit image
    R = 255.0
    
    # Compute PSNR
    psnr = 10 * np.log10((R ** 2) / mse)
    
    return psnr

# Prepare results
results = {name: {'qualities': [], 'psnr': [], 'size': []} for name in images}

for name, img in images.items():
    for q in qualities:
        filename = f"{name}_Q{q}.jpg"
        Image.fromarray(img).save(filename, "JPEG", quality=q)
        
        # Load compressed image
        compressed = Image.open(filename).convert('RGB')
        compressed_np=np.array(compressed)
        # File size in KB
        size_kb = os.path.getsize(filename) / 1024
        
        # Compute PSNR
        psnr = compute_psnr_y_channel(img, compressed_np)

        # Store results
        results[name]['qualities'].append(q)
        results[name]['psnr'].append(psnr)
        results[name]['size'].append(size_kb)

# Plotting
for name in images:
    plt.figure(figsize=(12, 5))

    # PSNR plot
    plt.subplot(1, 2, 1)
    plt.plot(results[name]['qualities'], results[name]['psnr'], marker='o')
    plt.title(f'{name} Image - PSNR vs Quality')
    plt.xlabel('JPEG Quality')
    plt.ylabel('PSNR (dB)')
    plt.grid(True)

    # File size plot
    plt.subplot(1, 2, 2)
    plt.plot(results[name]['qualities'], results[name]['size'], marker='o', color='orange')
    plt.title(f'{name} Image - File Size vs Quality')
    plt.xlabel('JPEG Quality')
    plt.ylabel('File Size (KB)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
#cleaning up jpg files
    for name in images:
        for q in qualities:
            os.remove(f"{name}_Q{q}.jpg")