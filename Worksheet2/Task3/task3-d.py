import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load original and received image
original = np.array(Image.open("original.jpg").convert("RGB"))
received = np.array(Image.open("received.jpg").convert("RGB"))


orig_h, orig_w = original.shape[:2]
recv_h, recv_w = received.shape[:2]

# crop of original picture
x_orig, y_orig, w_crop, h_crop = 1000, 2000, 300, 300

# Calculate relative positions
rel_x = x_orig / orig_w
rel_y = y_orig / orig_h
rel_w = w_crop / orig_w
rel_h = h_crop / orig_h

# Crop in received image
x_recv = int(rel_x * recv_w)
y_recv = int(rel_y * recv_h)
w_recv = int(rel_w * recv_w)
h_recv = int(rel_h * recv_h)

orig_crop = original[y_orig:y_orig+h_crop, x_orig:x_orig+w_crop]
recv_crop = received[y_recv:y_recv+h_recv, x_recv:x_recv+w_recv]

# Resize so its comparable
target_size = (min(orig_crop.shape[1], recv_crop.shape[1]),
               min(orig_crop.shape[0], recv_crop.shape[0]))

orig_crop_resized = cv2.resize(orig_crop, target_size)
recv_crop_resized = cv2.resize(recv_crop, target_size)

# calculate difference
difference = cv2.absdiff(orig_crop_resized, recv_crop_resized)

# show difference
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(orig_crop_resized)
plt.title("Original Patch")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(recv_crop_resized)
plt.title("Received Patch")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(difference)
plt.title("Difference")
plt.axis('off')

plt.tight_layout()
plt.show()
