import socket
import numpy as np
import cv2

def main():
    host = 'localhost'
    port = 9999

    s = socket.socket()
    print(f"Starting server on {host}:{port}")
    s.bind((host, port))
    s.listen(1)
    print("Now listening...")

    print("Waiting for sender...")
    conn, addr = s.accept()
    print("Connected by", addr)

    # Read length first
    img_size = int.from_bytes(conn.recv(8), 'big')

    # Read the image data
    data = b''
    while len(data) < img_size:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet

    # Decode image
    nparr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite('received.jpg', img)

    print("Received and saved as 'received.jpg'")
    conn.close()

if __name__ == '__main__':
    main()