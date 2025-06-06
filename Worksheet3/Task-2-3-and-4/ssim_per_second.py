import pandas as pd
import matplotlib.pyplot as plt
import glob
import re
import os

framerate = 24

pairs = [
    ("CRF18", "CBR1840"),
    ("CRF30", "CBR713"),
    ("CRF48", "CBR453"),
]

log_files = glob.glob("ssim_*.log")
dataframes = {}

# Regex to extract frame nr and ssim
pattern = re.compile(r"n:(\d+).*All:([0-9.]+)")

for log_file in log_files:
    label = os.path.splitext(os.path.basename(log_file))[0].replace("ssim_", "").upper()
    frames = []
    ssims = []

    with open(log_file, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                frame = int(match.group(1))
                ssim = float(match.group(2))
                frames.append(frame)
                ssims.append(ssim)

    df = pd.DataFrame({"frame": frames, "ssim": ssims})
    df["second"] = (df["frame"] / framerate).astype(int)
    dataframes[label] = df

# for boxplot later on
for label, df in dataframes.items():
    ssim_per_sec = df.groupby("second")["ssim"].mean().reset_index()
    ssim_per_sec.columns = ["second", "ssim"]
    ssim_per_sec.to_csv(f"ssim_{label}.csv", index=False)
    


# Plotting
fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
fig.suptitle("SSIM per Second (All channels)", fontsize=16)

for ax, (label1, label2) in zip(axes, pairs):
    for label in (label1, label2):
        df = dataframes.get(label)
        ssim_per_sec = df.groupby("second")["ssim"].mean()
        ax.plot(ssim_per_sec.index, ssim_per_sec.values, label=label)
        
    ax.set_title(f"{label1} vs {label2}")
    ax.set_ylabel("SSIM (All)")
    ax.grid(True)
    ax.legend()

axes[-1].set_xlabel("Time (seconds)")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


