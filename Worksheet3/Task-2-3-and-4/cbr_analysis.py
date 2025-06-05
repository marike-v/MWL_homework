import json
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# loading json data
with open("frames_453k.json", "r") as f:
    data_453k = json.load(f)

frame_counts_453k = Counter()
frame_bytes_453k = defaultdict(int)

for frame in data_453k['frames']:
    if 'pict_type' in frame and 'pkt_size' in frame:
        t = frame['pict_type']
        s = int(frame['pkt_size'])
        frame_counts_453k[t] += 1
        frame_bytes_453k[t] += s

total_frames_453k = sum(frame_counts_453k.values())
total_bytes_453k = sum(frame_bytes_453k.values())

frame_percent_453k = {k: v / total_frames_453k * 100 for k, v in frame_counts_453k.items()}
byte_percent_453k = {k: v / total_bytes_453k * 100 for k, v in frame_bytes_453k.items()}


with open("frames_1840k.json", "r") as f:
    data_1840k = json.load(f)

frame_counts_1840k = Counter()
frame_bytes_1840k = defaultdict(int)

for frame in data_1840k['frames']:
    if 'pict_type' in frame and 'pkt_size' in frame:
        t = frame['pict_type']
        s = int(frame['pkt_size'])
        frame_counts_1840k[t] += 1
        frame_bytes_1840k[t] += s

total_frames_1840k = sum(frame_counts_1840k.values())
total_bytes_1840k = sum(frame_bytes_1840k.values())

frame_percent_1840k = {k: v / total_frames_1840k * 100 for k, v in frame_counts_1840k.items()}
byte_percent_1840k = {k: v / total_bytes_1840k * 100 for k, v in frame_bytes_1840k.items()}

# plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# 453k Frame Count
axs[0, 0].pie(frame_percent_453k.values(), labels=frame_percent_453k.keys(), autopct='%1.1f%%')
axs[0, 0].set_title("CBR 453k – Frame Count (%)")

# 453k Byte Contribution
axs[0, 1].pie(byte_percent_453k.values(), labels=byte_percent_453k.keys(), autopct='%1.1f%%')
axs[0, 1].set_title("CBR 453k – Byte Contribution (%)")

# 1840k Frame Count
axs[1, 0].pie(frame_percent_1840k.values(), labels=frame_percent_1840k.keys(), autopct='%1.1f%%')
axs[1, 0].set_title("CBR 1840k – Frame Count (%)")

# 1840k Byte Contribution
axs[1, 1].pie(byte_percent_1840k.values(), labels=byte_percent_1840k.keys(), autopct='%1.1f%%')
axs[1, 1].set_title("CBR 1840k – Byte Contribution (%)")

plt.tight_layout()
plt.show()