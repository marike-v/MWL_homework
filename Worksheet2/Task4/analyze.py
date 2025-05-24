import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

# Load images
original = cv2.imread("lena.png")
received = cv2.imread("received.jpg")

# Resize received to match original
received = cv2.resize(received, (original.shape[1], original.shape[0]))

# Convert to grayscale for SSIM
gray_orig = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gray_recv = cv2.cvtColor(received, cv2.COLOR_BGR2GRAY)

# Calculate metrics
mse_value = np.mean((original - received) ** 2)
psnr_value = psnr(original, received)
ssim_value, _ = ssim(gray_orig, gray_recv, full=True)

# Plotting
plt.figure(figsize=(12, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')

# Received image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(received, cv2.COLOR_BGR2RGB))
plt.title("Received")
plt.axis('off')

plt.figtext(0.5, 0.01,
            f"MSE: {mse_value:.2f}    PSNR: {psnr_value:.2f} dB    SSIM: {ssim_value:.3f}",
            wrap=True, horizontalalignment='center', fontsize=12)

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.show()