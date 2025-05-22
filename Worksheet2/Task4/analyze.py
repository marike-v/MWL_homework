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
mse_val = np.mean((gray_orig - gray_recv) ** 2)
psnr_val = psnr(original, received)
ssim_val, _ = ssim(gray_orig, gray_recv, full=True)

print(f"MSE: {mse_val:.2f}")
print(f"PSNR: {psnr_val:.2f} dB")
print(f"SSIM: {ssim_val:.3f}")

# Show side-by-side
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(received, cv2.COLOR_BGR2RGB))
plt.title("Received")
plt.axis('off')

plt.tight_layout()
plt.show()