import cv2
import os 
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize

# ---------------------- load images from folder ----------------------
script_dir = os.path.dirname(__file__)

def load_rgb_image(filename):
    path = os.path.join(script_dir, filename)
    image_bgr = cv2.imread(path) #bgr is open cv default
    if image_bgr is None:
        raise FileNotFoundError(f"could not load {filename}")
    return cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# ---------------------- load images ----------------------
lena_rgb = load_rgb_image("lena.png")
landscape_rgb = load_rgb_image("landscape.png") 

# ---------------------- task (a): visualize lena channels ----------------------
# split into RGB channels
R, G, B = cv2.split(lena_rgb)

# plot color channels
plt.figure(figsize=(12, 4))
titles = ['Red Channel', 'Green Channel', 'Blue Channel']
channels = [R, G, B]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(channels[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

# plot histograms of channels
plt.figure(figsize=(12, 4))
colors = ['red', 'green', 'blue']

for i, channel in enumerate([R, G, B]):
    plt.subplot(1, 3, i+1)
    plt.hist(channel.ravel(), bins=256, color=colors[i], alpha=0.7)
    plt.title(f'{titles[i]} Histogram')
    plt.xlabel('Intensity Value')
    plt.ylabel('Pixel Count')
plt.tight_layout()
plt.show()

# ---------------------- Task (b): compute entropy ----------------------

#helper function to calculate entropy
def calculate_entropy(channel):
    hist, _ = np.histogram(channel, bins=256, range=(0, 256), density=True)
    hist_nonzero = hist[hist > 0]
    entropy = -np.sum(hist_nonzero * np.log2(hist_nonzero))
    return entropy


# lena channels
lena_R, lena_G, lena_B = cv2.split(lena_rgb)
# landscape channels
land_R, land_G, land_B = cv2.split(landscape_rgb)

# calculate and print entropy
print("entropy for lena (RGB):")
print("  R:", calculate_entropy(lena_R))
print("  G:", calculate_entropy(lena_G))
print("  B:", calculate_entropy(lena_B))

print("\nentropy for landscape (RGB):")
print("  R:", calculate_entropy(land_R))
print("  G:", calculate_entropy(land_G))
print("  B:", calculate_entropy(land_B))


# ---------------------- Task (c): YCbCr transformation and plotting ----------------------

def convert_to_ycbcr(image_rgb):
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    image_ycbcr = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YCrCb)  
    Y, Cr, Cb = cv2.split(image_ycbcr)
    return Y, Cb, Cr  # return in Y, Cb, Cr order

# convert both images to YCbCr
lena_Y, lena_Cb, lena_Cr = convert_to_ycbcr(lena_rgb)
land_Y, land_Cb, land_Cr = convert_to_ycbcr(landscape_rgb)

# --- plot YCbCr components for lena ---
plt.figure(figsize=(12, 4))
lena_ycc_titles = ['Luma (Y)', 'Chroma Blue (Cb)', 'Chroma Red (Cr)']
lena_ycc_channels = [lena_Y, lena_Cb, lena_Cr]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(lena_ycc_channels[i], cmap='gray')
    plt.title(f"Lena - {lena_ycc_titles[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()

# plot histograms for lena
plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.hist(lena_ycc_channels[i].ravel(), bins=256, color='gray', alpha=0.7)
    plt.title(f"Lena - {lena_ycc_titles[i]} Histogram")
    plt.xlabel('Intensity Value')
    plt.ylabel('Pixel Count')
plt.tight_layout()
plt.show()

# --- plot YCbCr components for landscape ---
plt.figure(figsize=(12, 4))
land_ycc_titles = ['Luma (Y)', 'Chroma Blue (Cb)', 'Chroma Red (Cr)']
land_ycc_channels = [land_Y, land_Cb, land_Cr]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(land_ycc_channels[i], cmap='gray')
    plt.title(f"Landscape - {land_ycc_titles[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()

# plot histograms for landscape
plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.hist(land_ycc_channels[i].ravel(), bins=256, color='gray', alpha=0.7)
    plt.title(f"Landscape - {land_ycc_titles[i]} Histogram")
    plt.xlabel('Intensity Value')
    plt.ylabel('Pixel Count')
plt.tight_layout()
plt.show()

# ---------------------- Task (d): entropy of Y, Cb, Cr ----------------------

# lena YCbCr entropies
lena_Y_entropy = calculate_entropy(lena_Y)
lena_Cb_entropy = calculate_entropy(lena_Cb)
lena_Cr_entropy = calculate_entropy(lena_Cr)

# landscape YCbCr entropies
land_Y_entropy = calculate_entropy(land_Y)
land_Cb_entropy = calculate_entropy(land_Cb)
land_Cr_entropy = calculate_entropy(land_Cr)

# print results
print("\nentropy for lena (YCbCr):")
print("  Y :", lena_Y_entropy)
print("  Cb:", lena_Cb_entropy)
print("  Cr:", lena_Cr_entropy)

print("\nentropy for landscape (YCbCr):")
print("  Y :", land_Y_entropy)
print("  Cb:", land_Cb_entropy)
print("  Cr:", land_Cr_entropy)



# ---------------------- Task (f): subsampling ----------------------

# function to downsample and upsample Cb and Cr
def subsample_and_reconstruct(Y, Cb, Cr, mode="4:4:4"):
    h, w = Y.shape

    if mode == "4:4:4":
        Cb_ds = Cb
        Cr_ds = Cr

    elif mode == "4:2:2":
        Cb_ds = Cb[:, ::2]  # half width
        Cr_ds = Cr[:, ::2]
        Cb_ds = np.repeat(Cb_ds, 2, axis=1)  # upsample back
        Cr_ds = np.repeat(Cr_ds, 2, axis=1)

    elif mode == "4:2:0":
        Cb_ds = Cb[::2, ::2]  # half height and width
        Cr_ds = Cr[::2, ::2]
        Cb_ds = np.repeat(np.repeat(Cb_ds, 2, axis=0), 2, axis=1)
        Cr_ds = np.repeat(np.repeat(Cr_ds, 2, axis=0), 2, axis=1)

    # ensure resized to match Y shape
    Cb_ds = resize(Cb_ds, (h, w), anti_aliasing=True, preserve_range=True).astype(np.uint8)
    Cr_ds = resize(Cr_ds, (h, w), anti_aliasing=True, preserve_range=True).astype(np.uint8)

    # merge and convert back to BGR, RGB
    ycrcb = cv2.merge([Y, Cr_ds, Cb_ds])  
    bgr = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return rgb, Cb_ds, Cr_ds

# convert lena to YCrCb
lena_ycrcb = cv2.cvtColor(cv2.cvtColor(lena_rgb, cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(lena_ycrcb)

# reconstruct all versions
lena_444, Cb_444, Cr_444 = subsample_and_reconstruct(Y, Cb, Cr, "4:4:4")
lena_422, Cb_422, Cr_422 = subsample_and_reconstruct(Y, Cb, Cr, "4:2:2")
lena_420, Cb_420, Cr_420 = subsample_and_reconstruct(Y, Cb, Cr, "4:2:0")

# plot all images side-by-side
plt.figure(figsize=(12, 4))
titles = ["4:4:4 (Original)", "4:2:2", "4:2:0"]
images = [lena_444, lena_422, lena_420]
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.show()

# compute and print entropies
print("\n entropy for lena with different subsampling:")
for label, Cb_, Cr_ in zip(titles, [Cb_444, Cb_422, Cb_420], [Cr_444, Cr_422, Cr_420]):
    Y_entropy = calculate_entropy(Y)
    Cb_entropy = calculate_entropy(Cb_)
    Cr_entropy = calculate_entropy(Cr_)
    total = Y_entropy + Cb_entropy + Cr_entropy
    print(f"{label}")
    print(f"  Y:  {Y_entropy:.3f}")
    print(f"  Cb: {Cb_entropy:.3f}")
    print(f"  Cr: {Cr_entropy:.3f}")
    print(f"  total entropy (Y + Cb + Cr): {total:.3f}\n")