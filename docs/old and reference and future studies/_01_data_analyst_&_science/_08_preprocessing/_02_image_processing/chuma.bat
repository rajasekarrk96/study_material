@echo off
rem Create the main folder for Image Processing
mkdir "Image Processing"

rem Create topics and subtopics for Image Processing
cd "Image Processing"

rem 1. Introduction to Image Processing
mkdir "01. Introduction to Image Processing"
mkdir "01. Introduction to Image Processing\_01_ Definition and Importance of Image Processing"
mkdir "01. Introduction to Image Processing\_02_ Applications in Machine and Deep Learning"
mkdir "01. Introduction to Image Processing\_03_ Key Tools and Libraries"
mkdir "01. Introduction to Image Processing\_03_ Key Tools and Libraries\_01_ OpenCV"
mkdir "01. Introduction to Image Processing\_03_ Key Tools and Libraries\_02_ PIL"
mkdir "01. Introduction to Image Processing\_03_ Key Tools and Libraries\_03_ Scikit-Image"

rem 2. Basics of Image Processing
mkdir "02. Basics of Image Processing"
mkdir "02. Basics of Image Processing\_01_ Image Formats and Representation"
mkdir "02. Basics of Image Processing\_01_ Image Formats and Representation\_01_ Raster vs. Vector Images"
mkdir "02. Basics of Image Processing\_01_ Image Formats and Representation\_02_ Color Spaces"
mkdir "02. Basics of Image Processing\_01_ Image Formats and Representation\_03_ File Formats"
mkdir "02. Basics of Image Processing\_02_ Image Operations"
mkdir "02. Basics of Image Processing\_02_ Image Operations\_01_ Reading and Displaying Images"
mkdir "02. Basics of Image Processing\_02_ Image Operations\_02_ Resizing and Cropping"
mkdir "02. Basics of Image Processing\_02_ Image Operations\_03_ Image Rotation and Translation"
mkdir "02. Basics of Image Processing\_02_ Image Operations\_04_ Flipping and Mirroring"
mkdir "02. Basics of Image Processing\_03_ Image Histogram"
mkdir "02. Basics of Image Processing\_03_ Image Histogram\_01_ Understanding Image Histograms"
mkdir "02. Basics of Image Processing\_03_ Image Histogram\_02_ Histogram Equalization"
mkdir "02. Basics of Image Processing\_04_ Image Filtering"
mkdir "02. Basics of Image Processing\_04_ Image Filtering\_01_ Linear Filters"
mkdir "02. Basics of Image Processing\_04_ Image Filtering\_02_ Non-linear Filters"

rem 3. Feature Detection and Extraction
mkdir "03. Feature Detection and Extraction"
mkdir "03. Feature Detection and Extraction\_01_ Edge Detection"
mkdir "03. Feature Detection and Extraction\_01_ Edge Detection\_01_ Sobel and Scharr Operators"
mkdir "03. Feature Detection and Extraction\_01_ Edge Detection\_02_ Canny Edge Detection"
mkdir "03. Feature Detection and Extraction\_01_ Edge Detection\_03_ Laplacian of Gaussian"
mkdir "03. Feature Detection and Extraction\_02_ Corner Detection"
mkdir "03. Feature Detection and Extraction\_02_ Corner Detection\_01_ Harris Corner Detection"
mkdir "03. Feature Detection and Extraction\_02_ Corner Detection\_02_ Shi-Tomasi Corner Detection"
mkdir "03. Feature Detection and Extraction\_03_ Keypoint Detection and Description"
mkdir "03. Feature Detection and Extraction\_03_ Keypoint Detection and Description\_01_ SIFT"
mkdir "03. Feature Detection and Extraction\_03_ Keypoint Detection and Description\_02_ SURF"
mkdir "03. Feature Detection and Extraction\_03_ Keypoint Detection and Description\_03_ ORB"

rem 4. Image Transformation
mkdir "04. Image Transformation"
mkdir "04. Image Transformation\_01_ Geometric Transformations"
mkdir "04. Image Transformation\_01_ Geometric Transformations\_01_ Scaling and Rotation"
mkdir "04. Image Transformation\_01_ Geometric Transformations\_02_ Perspective and Affine Transformations"
mkdir "04. Image Transformation\_02_ Image Thresholding"
mkdir "04. Image Transformation\_02_ Image Thresholding\_01_ Simple Thresholding"
mkdir "04. Image Transformation\_02_ Image Thresholding\_02_ Adaptive Thresholding"
mkdir "04. Image Transformation\_02_ Image Thresholding\_03_ Otsu’s Thresholding"
mkdir "04. Image Transformation\_03_ Morphological Operations"
mkdir "04. Image Transformation\_03_ Morphological Operations\_01_ Erosion and Dilation"
mkdir "04. Image Transformation\_03_ Morphological Operations\_02_ Opening and Closing"
mkdir "04. Image Transformation\_03_ Morphological Operations\_03_ Morphological Gradient"

rem 5. Image Segmentation
mkdir "05. Image Segmentation"
mkdir "05. Image Segmentation\_01_ Traditional Segmentation Techniques"
mkdir "05. Image Segmentation\_01_ Traditional Segmentation Techniques\_01_ Region-Based Segmentation"
mkdir "05. Image Segmentation\_01_ Traditional Segmentation Techniques\_02_ Edge-Based Segmentation"
mkdir "05. Image Segmentation\_02_ Advanced Segmentation"
mkdir "05. Image Segmentation\_02_ Advanced Segmentation\_01_ Watershed Algorithm"
mkdir "05. Image Segmentation\_02_ Advanced Segmentation\_02_ GrabCut Algorithm"
mkdir "05. Image Segmentation\_03_ Deep Learning-based Segmentation"
mkdir "05. Image Segmentation\_03_ Deep Learning-based Segmentation\_01_ Semantic Segmentation"
mkdir "05. Image Segmentation\_03_ Deep Learning-based Segmentation\_02_ Instance Segmentation"
mkdir "05. Image Segmentation\_03_ Deep Learning-based Segmentation\_03_ Panoptic Segmentation"

rem 6. Object Detection
mkdir "06. Object Detection"
mkdir "06. Object Detection\_01_ Traditional Object Detection Methods"
mkdir "06. Object Detection\_01_ Traditional Object Detection Methods\_01_ Haar Cascades"
mkdir "06. Object Detection\_01_ Traditional Object Detection Methods\_02_ HOG"
mkdir "06. Object Detection\_02_ Deep Learning-based Object Detection"
mkdir "06. Object Detection\_02_ Deep Learning-based Object Detection\_01_ YOLO"
mkdir "06. Object Detection\_02_ Deep Learning-based Object Detection\_02_ SSD"
mkdir "06. Object Detection\_02_ Deep Learning-based Object Detection\_03_ Faster R-CNN"
mkdir "06. Object Detection\_02_ Deep Learning-based Object Detection\_04_ EfficientDet"

rem 7. Image Classification
mkdir "07. Image Classification"
mkdir "07. Image Classification\_01_ Machine Learning Approaches"
mkdir "07. Image Classification\_01_ Machine Learning Approaches\_01_ Feature Engineering"
mkdir "07. Image Classification\_01_ Machine Learning Approaches\_02_ SVM and Decision Trees"
mkdir "07. Image Classification\_02_ Deep Learning Approaches"
mkdir "07. Image Classification\_02_ Deep Learning Approaches\_01_ CNN Architectures"
mkdir "07. Image Classification\_02_ Deep Learning Approaches\_02_ Pre-trained Models"
mkdir "07. Image Classification\_03_ Transfer Learning"
mkdir "07. Image Classification\_03_ Transfer Learning\_01_ Fine-tuning Pre-trained Models"

rem 8. Image Augmentation
mkdir "08. Image Augmentation"
mkdir "08. Image Augmentation\_01_ Flip, Rotate, Crop"
mkdir "08. Image Augmentation\_02_ Noise Injection"
mkdir "08. Image Augmentation\_03_ Color Jitter"
mkdir "08. Image Augmentation\_04_ Advanced Augmentation"
mkdir "08. Image Augmentation\_04_ Advanced Augmentation\_01_ CutMix"
mkdir "08. Image Augmentation\_04_ Advanced Augmentation\_02_ MixUp"
mkdir "08. Image Augmentation\_04_ Advanced Augmentation\_03_ Random Erasing"

rem 9. Generative Models
mkdir "09. Generative Models"
mkdir "09. Generative Models\_01_ Generative Adversarial Networks"
mkdir "09. Generative Models\_01_ Generative Adversarial Networks\_01_ DCGAN"
mkdir "09. Generative Models\_01_ Generative Adversarial Networks\_02_ CycleGAN"
mkdir "09. Generative Models\_01_ Generative Adversarial Networks\_03_ StyleGAN"
mkdir "09. Generative Models\_02_ Variational Autoencoders"
mkdir "09. Generative Models\_02_ Variational Autoencoders\_01_ Applications in Image Synthesis"
mkdir "09. Generative Models\_03_ Diffusion Models"
mkdir "09. Generative Models\_03_ Diffusion Models\_01_ Denoising Diffusion Probabilistic Models"

rem 10. Advanced Image Processing Techniques
mkdir "10. Advanced Image Processing Techniques"
mkdir "10. Advanced Image Processing Techniques\_01_ Super-Resolution"
mkdir "10. Advanced Image Processing Techniques\_01_ Super-Resolution\_01_ ESRGAN"
mkdir "10. Advanced Image Processing Techniques\_02_ Image Denoising"
mkdir "10. Advanced Image Processing Techniques\_02_ Image Denoising\_01_ Autoencoders"
mkdir "10. Advanced Image Processing Techniques\_03_ Image Inpainting and Completion"
mkdir "10. Advanced Image Processing Techniques\_03_ Image Inpainting and Completion\_01_ Image-to-Image Translation"
mkdir "10. Advanced Image Processing Techniques\_03_ Image Inpainting and Completion\_02_ Pix2Pix"
mkdir "10. Advanced Image Processing Techniques\_03_ Image Inpainting and Completion\_03_ CycleGAN"

rem 11. Explainability in Image Models
mkdir "11. Explainability in Image Models"
mkdir "11. Explainability in Image Models\_01_ Saliency Maps"
mkdir "11. Explainability in Image Models\_02_ Grad-CAM"
mkdir "11. Explainability in Image Models\_03_ SHAP and LIME for CNNs"

rem 12. Image Processing for Specific Domains
mkdir "12. Image Processing for Specific Domains"
mkdir "12. Image Processing for Specific Domains\_01_ Medical Imaging"
mkdir "12. Image Processing for Specific Domains\_01_ Medical Imaging\_01_ CT Scan and MRI Analysis"
mkdir "12. Image Processing for Specific Domains\_01_ Medical Imaging\_02_ Cancer Detection"
mkdir "12. Image Processing for Specific Domains\_02_ Satellite Imaging"
mkdir "12. Image Processing for Specific Domains\_02_ Satellite Imaging\_01_ Remote Sensing and Land Cover Classification"
mkdir "12. Image Processing for Specific Domains\_03_ Autonomous Vehicles"
mkdir "12. Image Processing for Specific Domains\_03_ Autonomous Vehicles\_01_ Lane Detection"
mkdir "12. Image Processing for Specific Domains\_03_ Autonomous Vehicles\_02_ Object Tracking"
mkdir "12. Image Processing for Specific Domains\_04_ Facial Recognition"
mkdir "12. Image Processing for Specific Domains\_04_ Facial Recognition\_01_ Face Detection and Alignment"
mkdir "12. Image Processing for Specific Domains\_04_ Facial Recognition\_02_ Face Verification and Identification"

rem 13. Tools and Frameworks for Image Processing
mkdir "13. Tools and Frameworks for Image Processing"
mkdir "13. Tools and Frameworks for Image Processing\_01_ OpenCV"
mkdir "13. Tools and Frameworks for Image Processing\_02_ PyTorch and TensorFlow/Keras"
mkdir "13. Tools and Frameworks for Image Processing\_03_ Dlib"
mkdir "13. Tools and Frameworks for Image Processing\_04_ Albumentations"

echo Folders created successfully!
pause
