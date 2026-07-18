@echo off
rem Create the main folder for Video Processing
mkdir "Video Processing"

rem Create topics and subtopics for Video Processing
cd "Video Processing"

rem 1. Introduction to Video Processing
mkdir "01. Introduction to Video Processing"
mkdir "01. Introduction to Video Processing\_01_ Definition and Importance of Video Processing"
mkdir "01. Introduction to Video Processing\_02_ Applications in Machine and Deep Learning"
mkdir "01. Introduction to Video Processing\_03_ Key Tools and Libraries"
mkdir "01. Introduction to Video Processing\_03_ Key Tools and Libraries\_01_ OpenCV"
mkdir "01. Introduction to Video Processing\_03_ Key Tools and Libraries\_02_ FFmpeg"
mkdir "01. Introduction to Video Processing\_03_ Key Tools and Libraries\_03_ MoviePy"

rem 2. Basics of Video Processing
mkdir "02. Basics of Video Processing"
mkdir "02. Basics of Video Processing\_01_ Video Formats and Representation"
mkdir "02. Basics of Video Processing\_01_ Video Formats and Representation\_01_ Video Compression"
mkdir "02. Basics of Video Processing\_01_ Video Formats and Representation\_02_ Common Video File Formats"
mkdir "02. Basics of Video Processing\_02_ Video Operations"
mkdir "02. Basics of Video Processing\_02_ Video Operations\_01_ Reading and Writing Video Files"
mkdir "02. Basics of Video Processing\_02_ Video Operations\_02_ Frame Extraction and Manipulation"
mkdir "02. Basics of Video Processing\_02_ Video Operations\_03_ Video Frame Rate and Resolution"
mkdir "02. Basics of Video Processing\_03_ Video Resizing and Cropping"
mkdir "02. Basics of Video Processing\_03_ Video Resizing and Cropping\_01_ Scaling"
mkdir "02. Basics of Video Processing\_03_ Video Resizing and Cropping\_02_ Cropping Video Frames"
mkdir "02. Basics of Video Processing\_04_ Video Filters"
mkdir "02. Basics of Video Processing\_04_ Video Filters\_01_ Temporal and Spatial Filters"
mkdir "02. Basics of Video Processing\_04_ Video Filters\_02_ Noise Reduction in Videos"

rem 3. Video Feature Detection and Tracking
mkdir "03. Video Feature Detection and Tracking"
mkdir "03. Video Feature Detection and Tracking\_01_ Optical Flow"
mkdir "03. Video Feature Detection and Tracking\_01_ Optical Flow\_01_ Lucas-Kanade Optical Flow"
mkdir "03. Video Feature Detection and Tracking\_01_ Optical Flow\_02_ Farneback Optical Flow"
mkdir "03. Video Feature Detection and Tracking\_02_ Object Tracking"
mkdir "03. Video Feature Detection and Tracking\_02_ Object Tracking\_01_ KLT Tracker"
mkdir "03. Video Feature Detection and Tracking\_02_ Object Tracking\_02_ Median Flow Tracker"
mkdir "03. Video Feature Detection and Tracking\_02_ Object Tracking\_03_ CSRT Tracker"
mkdir "03. Video Feature Detection and Tracking\_03_ Background Subtraction"
mkdir "03. Video Feature Detection and Tracking\_03_ Background Subtraction\_01_ MOG2"
mkdir "03. Video Feature Detection and Tracking\_03_ Background Subtraction\_02_ KNN Background Subtraction"

rem 4. Video Analysis
mkdir "04. Video Analysis"
mkdir "04. Video Analysis\_01_ Motion Detection"
mkdir "04. Video Analysis\_01_ Motion Detection\_01_ Frame Differencing"
mkdir "04. Video Analysis\_01_ Motion Detection\_02_ Optical Flow for Motion Detection"
mkdir "04. Video Analysis\_02_ Video Segmentation"
mkdir "04. Video Analysis\_02_ Video Segmentation\_01_ Scene Segmentation"
mkdir "04. Video Analysis\_02_ Video Segmentation\_02_ Shot Boundary Detection"
mkdir "04. Video Analysis\_03_ Action Recognition"
mkdir "04. Video Analysis\_03_ Action Recognition\_01_ Traditional Methods"
mkdir "04. Video Analysis\_03_ Action Recognition\_02_ Deep Learning Approaches"

rem 5. Video Classification
mkdir "05. Video Classification"
mkdir "05. Video Classification\_01_ Machine Learning Approaches"
mkdir "05. Video Classification\_01_ Machine Learning Approaches\_01_ Feature Extraction from Videos"
mkdir "05. Video Classification\_01_ Machine Learning Approaches\_02_ SVM and Random Forest"
mkdir "05. Video Classification\_02_ Deep Learning Approaches"
mkdir "05. Video Classification\_02_ Deep Learning Approaches\_01_ CNN for Video Classification"
mkdir "05. Video Classification\_02_ Deep Learning Approaches\_02_ LSTM Networks"
mkdir "05. Video Classification\_02_ Deep Learning Approaches\_03_ 3D CNNs"
mkdir "05. Video Classification\_03_ Transfer Learning"
mkdir "05. Video Classification\_03_ Transfer Learning\_01_ Fine-tuning Pre-trained Networks"

rem 6. Object Detection in Video
mkdir "06. Object Detection in Video"
mkdir "06. Object Detection in Video\_01_ Object Detection Techniques"
mkdir "06. Object Detection in Video\_01_ Object Detection Techniques\_01_ YOLO in Video"
mkdir "06. Object Detection in Video\_01_ Object Detection Techniques\_02_ SSD in Video"
mkdir "06. Object Detection in Video\_01_ Object Detection Techniques\_03_ Faster R-CNN in Video"
mkdir "06. Object Detection in Video\_02_ Video Object Tracking"
mkdir "06. Object Detection in Video\_02_ Video Object Tracking\_01_ SORT Tracker"
mkdir "06. Object Detection in Video\_02_ Video Object Tracking\_02_ DeepSORT Tracker"

rem 7. Video Stabilization
mkdir "07. Video Stabilization"
mkdir "07. Video Stabilization\_01_ Traditional Stabilization Methods"
mkdir "07. Video Stabilization\_01_ Traditional Stabilization Methods\_01_ Transformation Estimation"
mkdir "07. Video Stabilization\_01_ Traditional Stabilization Methods\_02_ Video Registration"
mkdir "07. Video Stabilization\_02_ Deep Learning-based Stabilization"
mkdir "07. Video Stabilization\_02_ Deep Learning-based Stabilization\_01_ CNN for Video Stabilization"

rem 8. Video Generation
mkdir "08. Video Generation"
mkdir "08. Video Generation\_01_ Video Synthesis"
mkdir "08. Video Generation\_01_ Video Synthesis\_01_ DeepFake"
mkdir "08. Video Generation\_01_ Video Synthesis\_02_ Neural Style Transfer for Videos"
mkdir "08. Video Generation\_02_ Video Captioning"
mkdir "08. Video Generation\_02_ Video Captioning\_01_ Sequence-to-Sequence Models"
mkdir "08. Video Generation\_02_ Video Captioning\_02_ Transformer-based Models"

rem 9. Video Compression
mkdir "09. Video Compression"
mkdir "09. Video Compression\_01_ Traditional Compression Techniques"
mkdir "09. Video Compression\_01_ Traditional Compression Techniques\_01_ H.264"
mkdir "09. Video Compression\_01_ Traditional Compression Techniques\_02_ HEVC"
mkdir "09. Video Compression\_02_ Deep Learning-based Compression"
mkdir "09. Video Compression\_02_ Deep Learning-based Compression\_01_ Autoencoders for Video Compression"

rem 10. Video Enhancement
mkdir "10. Video Enhancement"
mkdir "10. Video Enhancement\_01_ Super-Resolution in Video"
mkdir "10. Video Enhancement\_01_ Super-Resolution in Video\_01_ Video SRGAN"
mkdir "10. Video Enhancement\_02_ Denoising in Video"
mkdir "10. Video Enhancement\_02_ Denoising in Video\_01_ Video Denoising with Deep Learning"
mkdir "10. Video Enhancement\_03_ Frame Interpolation"
mkdir "10. Video Enhancement\_03_ Frame Interpolation\_01_ Slow Motion Generation"

rem 11. Advanced Video Techniques
mkdir "11. Advanced Video Techniques"
mkdir "11. Advanced Video Techniques\_01_ Video Summarization"
mkdir "11. Advanced Video Techniques\_01_ Video Summarization\_01_ Keyframe Extraction"
mkdir "11. Advanced Video Techniques\_01_ Video Summarization\_02_ Temporal Segmentation"
mkdir "11. Advanced Video Techniques\_02_ Video Retrieval"
mkdir "11. Advanced Video Techniques\_02_ Video Retrieval\_01_ Content-based Video Retrieval"
mkdir "11. Advanced Video Techniques\_02_ Video Retrieval\_02_ Video Search with Deep Learning"

rem 12. Explainability in Video Models
mkdir "12. Explainability in Video Models"
mkdir "12. Explainability in Video Models\_01_ Feature Attribution Methods"
mkdir "12. Explainability in Video Models\_02_ Grad-CAM for Video"
mkdir "12. Explainability in Video Models\_03_ SHAP and LIME for Video Models"

echo Folders created successfully!
pause
