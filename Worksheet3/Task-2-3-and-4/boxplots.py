import pandas as pd
import matplotlib.pyplot as plt
import glob
import os


pairs = [("CRF18", "CBR1840"), ("CRF30", "CBR713"), ("CRF48", "CBR453")]


bitrate_data = {}
ssim_data = {}


for filepath in glob.glob("bitrate_*.csv"):
    label = os.path.splitext(os.path.basename(filepath))[0].replace("bitrate_", "").upper()
    df = pd.read_csv(filepath)
    bitrate_data[label] = df["bitrate_kbps"] if "bitrate_kbps" in df else df.iloc[:, 0]

for filepath in glob.glob("ssim_*.csv"):
    label = os.path.splitext(os.path.basename(filepath))[0].replace("ssim_", "").upper()
    df = pd.read_csv(filepath)
    ssim_data[label] = df["ssim"] if "ssim" in df else df.iloc[:, 0]

# plotting
fig, axes = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle("Boxplots of Bitrate and SSIM per Video (CRF vs CBR)", fontsize=16)

for i, (crf_label, cbr_label) in enumerate(pairs):
    # Bitrate boxplot
    bitrate_vals = [bitrate_data[crf_label], bitrate_data[cbr_label]]
    axes[i, 0].boxplot(bitrate_vals, labels=[crf_label, cbr_label])
    axes[i, 0].set_title(f"Bitrate: {crf_label} vs {cbr_label}")
    axes[i, 0].set_ylabel("Bitrate (kbps)")

    # SSIM boxplot
    ssim_vals = [ssim_data[crf_label], ssim_data[cbr_label]]
    axes[i, 1].boxplot(ssim_vals, labels=[crf_label, cbr_label])
    axes[i, 1].set_title(f"SSIM: {crf_label} vs {cbr_label}")
    axes[i, 1].set_ylabel("SSIM")

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()