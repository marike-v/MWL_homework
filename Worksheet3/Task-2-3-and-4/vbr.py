import os
import subprocess


input_video = 'big_buck_bunny_480p_surround-fix.avi'
output_dir = 'encoded_videos'
crf_values = [18, 24, 30, 36, 42, 48]

os.makedirs(output_dir, exist_ok=True)

# Encoding with different crfs
for crf in crf_values:
    output_path = os.path.join(output_dir, f'output_crf{crf}.mp4')
    command = [
        'ffmpeg',
        '-i', input_video,
        '-vcodec', 'libx264',
        '-crf', str(crf),
        '-preset', 'medium',
        '-y',  
        output_path
    ]
    subprocess.run(command)


