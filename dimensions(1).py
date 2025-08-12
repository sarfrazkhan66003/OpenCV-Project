import cv2

image = cv2.imread("Phase 1 /python_image.png")

if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Could not load image")