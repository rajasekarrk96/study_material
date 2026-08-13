# OpenCV — Master Syllabus

**Target Role:** Computer Vision Engineer / Edge AI Developer / Robotics Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 15 Hours  
**Prerequisites:** foundations/core-python, technologies/python-data-science  
**Required Courses:** foundations/core-python, technologies/python-data-science  
**Optional Courses:** foundations/raspberry-pi, foundations/esp32  

---

## Study Flow

### Module 1 — OpenCV Core Architecture & Color Spaces
1. **OpenCV Environment & Matrix Representation** (`cv2.imread`, `cv2.imshow`, NumPy array representation, channel order BGR vs RGB)
2. **Color Space Conversions** (BGR to Grayscale, HSV, LAB, RGB, color segmentation using HSV thresholds)
3. **Drawing Primitives & Annotations** (`cv2.line`, `cv2.rectangle`, `cv2.circle`, `cv2.putText`, rendering bounding boxes)

### Module 2 — Geometric Transformations & Image Processing
1. **Geometric Transforms** (Resizing, Affine transformations, Rotation matrix `getRotationMatrix2D`, Perspective warp `warpPerspective`)
2. **Image Filtering & Blurring** (Gaussian blur, Median blur, Bilateral filtering for edge-preserving smoothing)
3. **Morphological Operations** (Dilation, Erosion, Opening, Closing, Morphological Gradient)

### Module 3 — Edge Detection, Thresholding & Contours
1. **Image Thresholding** (Binary thresholding, Otsu's thresholding, Adaptive thresholding)
2. **Edge Detection Gradients** (Sobel, Scharr, Laplacian, Canny edge detector)
3. **Contour Extraction & Shape Analysis** (`findContours`, `drawContours`, contour area, perimeter, bounding rects, Convex Hull)

### Module 4 — Feature Detection & Matching
1. **Corner & Feature Detection** (Harris corner detector, Shi-Tomasi, FAST, ORB keypoints)
2. **Descriptor Extractors & Feature Matching** (ORB descriptors, Brute-Force Matcher, FLANN-based matching, RANSAC homography)
3. **Template Matching** (`cv2.matchTemplate`, template matching methods, multi-scale template matching)

### Module 5 — Video Streams & Camera Interfacing
1. **Video Capture & Streaming** (`cv2.VideoCapture`, USB camera feeds, RTSP streams, IP webcam ingestion)
2. **Video Writing & FPS Benchmarking** (`cv2.VideoWriter`, codec configuration like FourCC, calculating real-time FPS)
3. **Background Subtraction & Motion Detection** (MOG2, KNN background subtractor, detecting moving objects in video)
