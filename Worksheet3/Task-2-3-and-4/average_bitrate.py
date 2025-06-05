import os
import cv2
import matplotlib.pyplot as plt

output_dir = 'encoded_videos' 
bitrates = {} # using dictionary because we can make sure that each video gets mapped correctly to the corresponding bitrate


# iterating through all videos
for filename in sorted(os.listdir(output_dir)):
    
    crf = int(filename.split('crf')[1].split('.')[0])
    filepath = os.path.join(output_dir, filename)

    # open vides
    cap = cv2.VideoCapture(filepath)
    if not cap.isOpened():
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.release()

    if fps == 0:
        continue

    duration = frames / fps
    size_bytes = os.path.getsize(filepath)
    bitrate_kbps = (size_bytes * 8) / 1000 / duration  # Average bitrate

    bitrates[crf] = bitrate_kbps

crf_values = sorted(bitrates.keys())
bitrate_values = [bitrates[crf] for crf in crf_values]

# plotting
plt.plot(crf_values, bitrate_values, marker='o')
plt.title("Bitrate vs. CRF")
plt.xlabel("CRF")
plt.ylabel("Average Bitrate (kbps)")
plt.grid(True)
plt.show()