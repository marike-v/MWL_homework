import socket
import cv2
import numpy as np
import argparse
import io
import random

def add_noise(img, amount=0.01):
    noise = np.random.randn(*img.shape) * 255 * amount
    noisy_img = np.clip(img + noise, 0, 255).astype(np.uint8)
    return noisy_img

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, default='lena.png')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=9999)
    parser.add_argument('--quality', type=int, default=90)
    parser.add_argument('--noise', type=float, default=0.0)
    args = parser.parse_args()

    # Load image
    img = cv2.imread(args.image)
   

    if args.noise > 0:
        img = add_noise(img, args.noise)

    # Encode image as JPEG
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), args.quality]
    _, img_encoded = cv2.imencode('.jpg', img, encode_param)

    # Start socket
    s = socket.socket()


    s.connect((args.host, args.port))

    # Send length first
    s.send(len(img_encoded).to_bytes(8, 'big'))
    s.sendall(img_encoded.tobytes())

    print(f"Sent image ({len(img_encoded)} bytes) with JPEG quality={args.quality} and noise={args.noise}")
    s.close()

if __name__ == '__main__':
    main()
