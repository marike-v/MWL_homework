import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

pairs = [
    ("CRF18", "CBR1840"),
    ("CRF30", "CBR713"),
    ("CRF48", "CBR453"),
]

csv_files = glob.glob("packets_*.csv")
dataframes = {}

for csv_file in csv_files:
    label = os.path.splitext(os.path.basename(csv_file))[0].replace("packets_", "").upper()
    df = pd.read_csv(csv_file, names=["pts_time", "size"])
    df["second"] = df["pts_time"].astype(float).astype(int)
    dataframes[label] = df

# for boxplot later on
for label in dataframes:
    df = dataframes[label]
    bitrate_per_sec = df.groupby("second")["size"].sum() * 8 / 1000  # kbps
    export_df = bitrate_per_sec.reset_index()
    export_df.columns = ["second", "bitrate_kbps"]
    export_df.to_csv(f"bitrate_{label}.csv", index=False)


fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
fig.suptitle("Bitrate per Second Comparison (CRF vs CBR)", fontsize=16)

for ax, (label1, label2) in zip(axes, pairs):
    for label in (label1, label2):
        df = dataframes.get(label)
        bitrate_per_sec = df.groupby("second")["size"].sum() * 8 / 1000  # kbps
        ax.plot(bitrate_per_sec.index, bitrate_per_sec.values, label=label)
        

    ax.set_title(f"{label1} vs {label2}")
    ax.set_ylabel("Bitrate (kbps)")
    ax.legend()
    ax.grid(True)

axes[-1].set_xlabel("Time (seconds)")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()