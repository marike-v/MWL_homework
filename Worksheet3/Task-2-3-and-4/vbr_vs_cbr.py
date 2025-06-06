import matplotlib.pyplot as plt
import numpy as np

# metrics obtained from ffmpeg terminal output
video_metrics = {
    "CRF18": {
        "psnr_avg": 47.125729,
        "ssim_all": 0.993128
    },
    "CRF30": {
        "psnr_avg": 40.131047,
        "ssim_all": 0.974722
    },
    "CRF48": {
        "psnr_avg": 29.681791,
        "ssim_all": 0.860354
    },
    "CBR1840": {
        "psnr_avg": 48.265914,
        "ssim_all": 0.994498
    },
    "CBR713": {
        "psnr_avg": 44.001470,
        "ssim_all": 0.987341
    },
    "CBR453": {
        "psnr_avg": 41.919617,
        "ssim_all": 0.981445
    }
}

pairs = [
    ("CRF18", "CBR1840"),
    ("CRF30", "CBR713"),
    ("CRF48", "CBR453"),
]

# plotting
fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=False)
fig.suptitle("PSNR and SSIM Comparison: CRF vs CBR", fontsize=16)

for i, (crf_label, cbr_label) in enumerate(pairs):
    ax = axes[i]
    labels = [crf_label, cbr_label]
    psnr_vals = [video_metrics[crf_label]["psnr_avg"], video_metrics[cbr_label]["psnr_avg"]]
    ssim_vals = [video_metrics[crf_label]["ssim_all"], video_metrics[cbr_label]["ssim_all"]]
    bar_width = 0.4
    x = np.arange(len(labels))
    ax.bar(x, psnr_vals, width=bar_width, label="PSNR (dB)", color="skyblue")
    ax2 = ax.twinx()
    ax2.plot(x, ssim_vals, color="darkorange", marker="o", label="SSIM", linewidth=2)
    ax2.set_ylim(0.8, 1.01)
    ax.set_title(f"{crf_label} vs {cbr_label}")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("PSNR (dB)")
    ax2.set_ylabel("SSIM")
    bars_labels, bars_handles = ax.get_legend_handles_labels()
    line_labels, line_handles = ax2.get_legend_handles_labels()
    ax2.legend(bars_labels + line_labels, bars_handles + line_handles, loc="lower center")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()