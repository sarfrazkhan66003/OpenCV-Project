# OpenCV-Project
🖼️ OpenCV Project – Image Processing & Computer Vision
Welcome to the OpenCV Project repository! 🎯 This project demonstrates the use of OpenCV for image processing, feature detection, and computer vision tasks.

📜 Algorithm Overview
Step-by-Step Flow:
📂 Load Input – Read the image or video using cv2.imread() or cv2.VideoCapture().
🎨 Preprocessing – Convert to grayscale, resize, or apply filters (e.g., Gaussian blur).
🔍 Feature Extraction – Detect edges (Canny), contours, or keypoints (ORB/SIFT).
🧠 Processing Logic – Apply transformations, object detection, or recognition.
💾 Output – Display results with cv2.imshow() or save with cv2.imwrite().
📏 Find Contours – Use cv2.findContours() to extract shapes.
📐 Approximate Polygon – Use cv2.approxPolyDP() to simplify contour points.
🏷️ Classify Shapes – Count polygon vertices to identify shape type:
       3 corners → Triangle
       4 corners → Rectangle
       5 corners → Pentagon
       More than 5 → Circle
🖊️ Label Output – Draw contours and put shape names on the image.
👀 Display Result – Show final processed image with labels.

1️⃣ Contour & Shape Detection (contour_fun.py)
Logic Flow:
Load image
Convert to grayscale
Apply binary threshold
Find contours with cv2.findContours()
Approximate shape using cv2.approxPolyDP()
Classify shape based on number of corners
Draw contours & label shapes

2️⃣ Bitwise Operations (bitwise_op.py)
Logic Flow:
Create black images using NumPy
Draw a circle on one image and rectangle on another

Apply:
cv2.bitwise_and() → Intersection
cv2.bitwise_or() → Union
cv2.bitwise_not() → Invert image
Display all results

3️⃣ Canny Edge Detection (canny_func.py)
Logic Flow:
Load image in grayscale
Apply cv2.Canny() with low & high threshold values
Display original & edge-detected images

4️⃣ Thresholding (threshold_func.py)
Logic Flow:
Load image in grayscale
Apply cv2.threshold() with a set threshold value
Pixels above threshold → White
Pixels below threshold → Black

5️⃣ Face, Eye & Smile Detection – face_eye_smile.py
Uses Haar Cascades to detect:
Faces 👤
Eyes 👀
Smiles 😄
Runs in real-time via webcam feed.

6️⃣ Gaussian Blur – gaussian_blur.py
Applies Gaussian blur for smooth image filtering.
7️⃣ Median Blur – median_b.py
Removes noise from an image using median filtering.

8️⃣ Image Sharpening – sharpeninig.py
Enhances image details using a custom sharpening kernel.
