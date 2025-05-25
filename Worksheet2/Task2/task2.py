import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import convolve2d

# ---------------------- load images from folder ----------------------
script_dir = os.path.dirname(__file__)

def load_rgb_image(filename):
    path = os.path.join(script_dir, filename)
    image_bgr = cv2.imread(path)  # OpenCV loads as BGR
    if image_bgr is None:
        raise FileNotFoundError(f"could not load {filename}")
    return cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# ---------------------- Task 2(a): fft on Y channel ----------------------

# Load Lena image (RGB)
lena_rgb = load_rgb_image("lena.png")

# Convert RGB → BGR → YCrCb
lena_bgr = cv2.cvtColor(lena_rgb, cv2.COLOR_RGB2BGR)
lena_ycrcb = cv2.cvtColor(lena_bgr, cv2.COLOR_BGR2YCrCb)

# Extract Y (luma) channel
Y = lena_ycrcb[:, :, 0]

# Confirm Y is loaded
print("Y channel shape:", Y.shape)

# Compute FFT and magnitude
f_transform = np.fft.fft2(Y)
f_magnitude = np.abs(f_transform)

# Apply fftshift
f_shifted = np.fft.fftshift(f_transform)
f_magnitude_shifted = np.abs(f_shifted)

# Plot FFT magnitude (with and without shift)
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(np.log1p(f_magnitude), cmap='gray')
plt.title("fft magnitude (unshifted)")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(np.log1p(f_magnitude_shifted), cmap='gray')
plt.title("fft magnitude (shifted)")
plt.axis('off')

plt.tight_layout()
plt.show()

# ---------------------- Task 2(b): mean filter ----------------------

def apply_mean_filter(image, n):
    kernel = np.ones((n, n), dtype=np.float32) / (n * n)
    filtered = convolve2d(image, kernel, mode='same', boundary='symm')
    return filtered.astype(np.uint8)

# try multiple kernel sizes
sizes = [3, 5, 7, 9, 11]
plt.figure(figsize=(15, 6))

for i, size in enumerate(sizes):
    filtered = apply_mean_filter(Y, size)
    plt.subplot(2, 3, i+1)
    plt.imshow(filtered, cmap='gray')
    plt.title(f"mean filter (n={size})")
    plt.axis('off')

plt.tight_layout()
plt.show()

# ---------------------- Task 2(c): add gaussian noise & fft ----------------------
def add_gaussian_noise(image, mean=0, std=10):
    noise = np.random.normal(mean, std, image.shape)
    noisy = image + noise
    noisy_clipped = np.clip(noisy, 0, 255).astype(np.uint8)
    return noisy_clipped

# add noise
Y_noise_10 = add_gaussian_noise(Y, std=10)
Y_noise_50 = add_gaussian_noise(Y, std=50)

# fft with shift
def fft_magnitude(image):
    f = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f)
    magnitude = np.log1p(np.abs(f_shift))
    return magnitude

mag_10 = fft_magnitude(Y_noise_10)
mag_50 = fft_magnitude(Y_noise_50)

# plot results
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(Y_noise_10, cmap='gray')
plt.title("noisy image (σ = 10)")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(mag_10, cmap='gray')
plt.title("fft magnitude (σ = 10)")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(Y_noise_50, cmap='gray')
plt.title("noisy image (σ = 50)")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(mag_50, cmap='gray')
plt.title("fft magnitude (σ = 50)")
plt.axis('off')

plt.tight_layout()
plt.show()
