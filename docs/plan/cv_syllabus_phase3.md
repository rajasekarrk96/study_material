# Phase 3: Computer Vision — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 3 of 8  
**Domain**: Computer Vision  
**Required Previous Phases**: Phase 1 (ML), Phase 2 (DL `_11_deep_learning`)  
**Folder Root**: `docs/curriculum/_12_computer_vision/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph

```
_10_machine_learning   (Phase 1)
    └─> _11_deep_learning  (Phase 2)
            └─> _12_computer_vision  ◄── THIS PHASE
```

Cross-phase reuse nodes (zero duplication):
- `DL.11_05` CNNs — fully extended in this phase, not re-taught
- `DL.11_07_06` ViT — extended for dense prediction
- `DL.11_07_09` DETR — extended for advanced detection
- `DL.11_08_06` Diffusion / `DL.11_08_07` Text-to-Image — extended for generative CV
- `DL.11_09_06` CLIP — zero-shot CV foundation
- `DL.11_10_02` Fine-tuning — applied to CV domain-specific tasks
- `ML.10_11` XAI — Grad-CAM, saliency maps reused

---

## Skills Gained (This Phase)

- Build production-grade image classification, detection, segmentation pipelines
- Implement optical character recognition (OCR) systems
- Design face recognition, re-identification, and verification systems
- Build scene understanding and 3D perception systems
- Apply domain-specific CV (medical, satellite, industrial, retail)
- Implement multimodal vision-language systems with CLIP, LLaVA
- Build real-time CV inference pipelines (RTSP, edge devices)
- Use image generation for data augmentation and synthetic training sets
- Evaluate and benchmark vision models at production scale

---

## Course Structure

```
_12_computer_vision/
├── _12_01_cv_foundations_and_image_processing/
├── _12_02_advanced_classification_and_retrieval/
├── _12_03_advanced_object_detection/
├── _12_04_advanced_segmentation/
├── _12_05_ocr_and_document_understanding/
├── _12_06_face_recognition_and_biometrics/
├── _12_07_3d_vision_and_point_clouds/
├── _12_08_vision_language_models/
├── _12_09_domain_specific_cv/
└── _12_10_industry_projects/
```

---

## MODULE 01 — CV Foundations and Image Processing

**Folder**: `_12_01_cv_foundations_and_image_processing/`  
**Lesson Count**: 8  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — Digital Image Fundamentals
**File**: `_12_01_01_digital_image_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Image representation | Pixel grids, RGB, RGBA, grayscale |
| Color spaces | RGB, HSV, LAB, YCbCr, HSL |
| Image data types | uint8, float32, normalized [0,1] vs [0,255] |
| OpenCV basics | `cv2.imread`, `cv2.imwrite`, `cv2.imshow` |
| PIL / Pillow | `Image.open`, `Image.convert`, `Image.save` |
| Image metadata | EXIF, DPI, bit depth |
| Batch loading | `torchvision.io.read_image`, `imageio` |

---

#### Lesson 01.02 — Image Transformations and Filtering
**File**: `_12_01_02_image_transformations_filtering.md`

| Topics | Subtopics |
|---|---|
| Geometric transforms | Resize, crop, rotate, flip, affine, perspective |
| Interpolation methods | Nearest, bilinear, bicubic, Lanczos |
| Convolution filters | Blur, sharpen, edge detection (Sobel, Laplacian) |
| Gaussian filter | Noise reduction, σ parameter |
| Median filter | Salt-and-pepper noise removal |
| Morphological operations | Erosion, dilation, opening, closing |
| `cv2.filter2D` | Custom kernel convolution |
| `cv2.warpAffine` / `cv2.warpPerspective` | Geometric correction |

---

#### Lesson 01.03 — Feature Detection and Descriptors
**File**: `_12_01_03_feature_detection_and_descriptors.md`

| Topics | Subtopics |
|---|---|
| Harris corner detector | Corner response function |
| Shi-Tomasi | `cv2.goodFeaturesToTrack` |
| SIFT | Scale-Invariant Feature Transform, keypoints + descriptors |
| SURF | Speeded-Up Robust Features |
| ORB | Oriented FAST + Rotated BRIEF, real-time |
| BRIEF | Binary descriptor |
| Feature matching | BFMatcher, FLANN, ratio test (Lowe's) |
| Homography | `cv2.findHomography`, `cv2.perspectiveTransform` |

---

#### Lesson 01.04 — Image Segmentation (Classical)
**File**: `_12_01_04_image_segmentation_classical.md`

| Topics | Subtopics |
|---|---|
| Thresholding | Global, Otsu's, Adaptive |
| Watershed algorithm | `cv2.watershed` |
| GrabCut | Semi-automatic foreground extraction |
| Superpixels | SLIC, `skimage.segmentation.slic` |
| Graph cuts | Energy minimization segmentation |
| Mean shift | Mode-seeking clustering |
| Contour detection | `cv2.findContours`, `cv2.drawContours` |

---

#### Lesson 01.05 — Optical Flow and Motion Analysis
**File**: `_12_01_05_optical_flow_motion_analysis.md`

| Topics | Subtopics |
|---|---|
| Dense optical flow | Farneback, `cv2.calcOpticalFlowFarneback` |
| Sparse optical flow | Lucas-Kanade, `cv2.calcOpticalFlowPyrLK` |
| Background subtraction | MOG2, KNN, `cv2.createBackgroundSubtractorMOG2` |
| Temporal difference | Frame differencing |
| Motion vectors | From video frames to motion heatmaps |
| `torchvision.models.optical_flow` | RAFT model |

---

#### Lesson 01.06 — Camera Models and Calibration
**File**: `_12_01_06_camera_models_calibration.md`

| Topics | Subtopics |
|---|---|
| Pinhole camera model | Intrinsic matrix K, focal length, principal point |
| Lens distortion | Radial, tangential coefficients |
| Camera calibration | Chessboard pattern, `cv2.calibrateCamera` |
| Undistortion | `cv2.undistort` |
| Stereo calibration | Baseline, epipolar geometry |
| Extrinsic matrix | Rotation + translation, world to camera |
| Projection matrix | Homogeneous coordinates |

---

#### Lesson 01.07 — Image Quality and Preprocessing
**File**: `_12_01_07_image_quality_preprocessing.md`

| Topics | Subtopics |
|---|---|
| Histogram equalization | `cv2.equalizeHist`, CLAHE |
| Denoising | `cv2.fastNlMeansDenoisingColored`, total variation |
| Super-resolution (classical) | Bicubic upsampling, frequency domain |
| Image normalization | Per-channel mean/std, ImageNet stats |
| Format conversion | JPEG, PNG, WebP, TIFF compression tradeoffs |
| Image hashing | pHash, dHash for deduplication |
| Quality metrics | SSIM, PSNR, LPIPS (for DL models) |

---

#### Lesson 01.08 — Video Processing and Streaming
**File**: `_12_01_08_video_processing_streaming.md`

| Topics | Subtopics |
|---|---|
| `cv2.VideoCapture` | File, camera, RTSP stream |
| Frame extraction | `cap.read()`, frame rate, seek |
| `cv2.VideoWriter` | Output video, codec, fps |
| Frame sampling | Uniform, key-frame, random |
| Video decoding | PyAV, decord, torchvision.io |
| RTSP / RTMP | IP camera streaming, GStreamer pipeline |
| WebRTC | Browser-based real-time video |

---

## MODULE 02 — Advanced Classification and Retrieval

**Folder**: `_12_02_advanced_classification_and_retrieval/`  
**Lesson Count**: 7  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — Fine-Grained Visual Classification
**File**: `_12_02_01_fine_grained_visual_classification.md`

| Topics | Subtopics |
|---|---|
| Fine-grained challenge | Subtle inter-class differences |
| Datasets | CUB-200, Stanford Cars, FGVC-Aircraft |
| Part-based models | Attention on discriminative parts |
| Bilinear pooling | Two-stream feature interaction |
| Higher-order pooling | CBAM, BAM, non-local networks |
| WS-DAN | Weakly supervised discriminative attention |
| Long-tail recognition | Class-balanced sampling, decoupled training |

---

#### Lesson 02.02 — Image Retrieval and Metric Learning
**File**: `_12_02_02_image_retrieval_metric_learning.md`

| Topics | Subtopics |
|---|---|
| Image retrieval | Feature extraction → ANN search |
| Metric learning | Contrastive loss, triplet loss, N-pair loss |
| Siamese networks | Pairwise similarity learning |
| ArcFace / CosFace | Angular margin losses |
| Embedding spaces | L2-normalized, cosine similarity |
| FAISS | `faiss.IndexFlatL2`, IVF, HNSW |
| `hnswlib` | Fast approximate nearest neighbor |
| Re-ranking | k-reciprocal re-ranking (RR) |

---

#### Lesson 02.03 — Hash-Based Image Search
**File**: `_12_02_03_hash_based_image_search.md`

| Topics | Subtopics |
|---|---|
| Locality-Sensitive Hashing | Random projections |
| Deep hashing | HashNet, GreedyHash |
| Product quantization | FAISS PQ index |
| Inverted file index | FAISS IVF |
| Binary embeddings | Hamming distance, memory efficiency |
| Billion-scale retrieval | FAISS GPU, IVFPQ, IVFOPQ |

---

#### Lesson 02.04 — Zero-Shot and Few-Shot Classification
**File**: `_12_02_04_zero_shot_few_shot_classification.md`

| Topics | Subtopics |
|---|---|
| Zero-shot classification | CLIP-based, class name as text query |
| `openclip.classify` | Zero-shot ImageNet benchmark |
| Few-shot with prototypes | Prototype networks, episode training |
| Meta-learning for CV | MAML for visual few-shot |
| DINO features for zero-shot | Semantic spatial features without labels |
| Dataset generalization | DomainNet, ImageNet-R, ImageNet-Sketch |

---

#### Lesson 02.05 — Image Anomaly Detection
**File**: `_12_02_05_image_anomaly_detection.md`

| Topics | Subtopics |
|---|---|
| Anomaly detection formulation | Unsupervised one-class problem |
| PatchCore | Memory bank of nominal patches |
| PaDiM | Gaussian modelling per patch position |
| SPADE | Nearest-neighbour feature distance |
| CutPaste | Self-supervised anomaly pretext task |
| `anomalib` | Unified anomaly detection library |
| MVTec AD dataset | Benchmark for industrial inspection |
| Per-pixel scoring | Anomaly map, threshold, ROC/AUROC |

---

#### Lesson 02.06 — Scene Classification and Understanding
**File**: `_12_02_06_scene_classification_understanding.md`

| Topics | Subtopics |
|---|---|
| Scene recognition | Places365 dataset, ResNet-Places |
| Global vs local features | Scene context, object composition |
| Attribute prediction | Multi-label attribute classification |
| Visual relationship detection | Subject-predicate-object triplets |
| Scene graphs | Node = object, edge = relationship |
| Visual question answering (intro) | Full detail in Vision-Language module |

---

#### Lesson 02.07 — Image Deduplication and Clustering
**File**: `_12_02_07_image_deduplication_clustering.md`

| Topics | Subtopics |
|---|---|
| Perceptual hashing | pHash, dHash, wHash |
| Near-duplicate detection | Hamming distance threshold |
| Deep embedding clustering | DEC, SCAN, DINO + k-means |
| Dataset cleaning | Label noise, noisy web data |
| `cleanvision` | Automated dataset quality issues |
| `clip-retrieval` | CLIP-based image clustering at scale |

---

## MODULE 03 — Advanced Object Detection

**Folder**: `_12_03_advanced_object_detection/`  
**Lesson Count**: 8  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — Detection Metrics and Benchmarks
**File**: `_12_03_01_detection_metrics_benchmarks.md`

| Topics | Subtopics |
|---|---|
| IoU | Intersection over Union variants: IoU, GIoU, DIoU, CIoU |
| mAP | Mean Average Precision, COCO metric |
| COCO evaluation | AP@0.5, AP@0.75, AP@0.5:0.95, AP_S/M/L |
| PASCAL VOC metric | AP@0.5 |
| NMS variants | Soft-NMS, WBF (Weighted Box Fusion) |
| `pycocotools` | Official COCO evaluation |
| LVIS benchmark | Long-tail detection evaluation |

---

#### Lesson 03.02 — Anchor-Free Detection
**File**: `_12_03_02_anchor_free_detection.md`

| Topics | Subtopics |
|---|---|
| Anchor-free motivation | Avoid anchor hyperparameter tuning |
| FCOS | Centerness map, per-pixel regression |
| CenterNet | Gaussian heatmap, object as keypoint |
| CornerNet | Top-left + bottom-right corner pairs |
| ATSS | Adaptive training sample selection |
| TOOD | Task-aligned one-stage detection |

---

#### Lesson 03.03 — YOLOv8/v9/v10 Deep Dive
**File**: `_12_03_03_yolo_deep_dive.md`

| Topics | Subtopics |
|---|---|
| YOLOv8 architecture | C2f block, decoupled head, task variants |
| YOLOv9 | GELAN, PGI (Programmable Gradient Information) |
| YOLOv10 | NMS-free, dual-label assignment |
| YOLO-NAS | Neural Architecture Search for YOLO |
| RT-DETR | Real-time DETR baseline |
| Model variants | nano, small, medium, large, xlarge |
| Training config | `data.yaml`, augmentation, mosaic |
| `ultralytics` API | `YOLO`, `train`, `val`, `predict`, `export` |

---

#### Lesson 03.04 — Transformer-Based Detection
**File**: `_12_03_04_transformer_based_detection.md`

| Topics | Subtopics |
|---|---|
| DETR full pipeline | End-to-end, no NMS |
| Deformable DETR | Deformable attention, fast convergence |
| DAB-DETR | Dynamic anchor boxes |
| DN-DETR | Denoising training |
| DINO-DETR | Contrastive denoising, SOTA on COCO |
| Co-DETR | Collaborative training |
| `transformers.AutoModelForObjectDetection` | HuggingFace interface |

---

#### Lesson 03.05 — Multi-Scale and Feature Pyramid Networks
**File**: `_12_03_05_multi_scale_feature_pyramid_networks.md`

| Topics | Subtopics |
|---|---|
| FPN | Top-down pathway, lateral connections |
| PANet | Bottom-up path augmentation |
| BiFPN | Weighted bidirectional FPN (EfficientDet) |
| PAFPN | YOLOv5/v8 neck variant |
| NAS-FPN | Searched feature pyramid |
| Scale-invariant detection | Small object detection strategies |

---

#### Lesson 03.06 — 3D Object Detection
**File**: `_12_03_06_3d_object_detection.md`

| Topics | Subtopics |
|---|---|
| LiDAR detection | Point cloud input, BEV representation |
| PointPillars | Pillars as pseudo-images |
| VoxelNet | Voxelized point cloud |
| CenterPoint | Heatmap-based 3D detection |
| Camera-based 3D | FCOS3D, PGD, BEVDet |
| Fusion-based | PointPainting, BEVFusion |
| nuScenes / KITTI | Benchmark datasets |

---

#### Lesson 03.07 — Rotated and Oriented Object Detection
**File**: `_12_03_07_rotated_oriented_object_detection.md`

| Topics | Subtopics |
|---|---|
| Oriented bounding boxes | (cx, cy, w, h, θ) representation |
| DOTA dataset | Aerial image benchmark |
| S2ANet | Feature alignment for oriented detection |
| Oriented R-CNN | Rotated RPN + RoI |
| `mmrotate` | OpenMMLab oriented detection toolkit |
| Applications | Satellite imagery, text, medical |

---

#### Lesson 03.08 — Real-Time Detection and Edge Deployment
**File**: `_12_03_08_real_time_detection_edge.md`

| Topics | Subtopics |
|---|---|
| Latency targets | FPS requirements per use case |
| Model selection | YOLOv8n vs MobileNetSSD vs NanoDetPlus |
| TensorRT optimization | FP16 engine, int8 calibration |
| OpenVINO | Intel hardware optimization |
| Hailo | Hailo-8 chip deployment |
| Jetson Nano / Orin | NVIDIA edge deployment |
| DeepStream | NVIDIA multi-stream inference pipeline |
| Benchmarking | `trtexec`, latency vs throughput tradeoffs |

---

## MODULE 04 — Advanced Segmentation

**Folder**: `_12_04_advanced_segmentation/`  
**Lesson Count**: 8  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — Semantic Segmentation Deep Dive
**File**: `_12_04_01_semantic_segmentation_deep_dive.md`

| Topics | Subtopics |
|---|---|
| FCN to modern methods | Encoder-decoder evolution |
| DeepLabV3+ | ASPP, decoder, `output_stride` |
| HRNet | High-resolution representation, multi-scale fusion |
| SegFormer | MiT backbone, lightweight decoder head |
| Segmenter | ViT backbone + mask Transformer |
| `mmsegmentation` | Config-based semantic segmentation |
| Evaluation | mIoU, pixel accuracy, frequency weighted IU |

---

#### Lesson 04.02 — Instance Segmentation Deep Dive
**File**: `_12_04_02_instance_segmentation_deep_dive.md`

| Topics | Subtopics |
|---|---|
| Mask R-CNN full pipeline | ROI Align → mask head |
| SOLOv2 | Instance-aware segmentation, no RPN |
| CondInst | Conditional convolutions for masks |
| QueryInst | DETR-based instance segmentation |
| EfficientSAM | Distilled SAM, faster |
| `detectron2` | Facebook Research toolkit |
| Evaluation | AP_mask, COCO instance segmentation |

---

#### Lesson 04.03 — Panoptic Segmentation
**File**: `_12_04_03_panoptic_segmentation.md`

| Topics | Subtopics |
|---|---|
| Panoptic definition | Things (instances) + Stuff (regions) |
| PanopticFPN | Unified semantic + instance |
| MaskFormer | Mask classification unified framework |
| Mask2Former | Cross-attention on query embeddings |
| K-Net | Kernel-based unified segmentation |
| PQ metric | Panoptic Quality = SQ × RQ |

---

#### Lesson 04.04 — Segment Anything Model (SAM)
**File**: `_12_04_04_segment_anything_model_sam.md`

| Topics | Subtopics |
|---|---|
| SAM architecture | Image encoder + Prompt encoder + Mask decoder |
| Prompt types | Points, boxes, masks, text (via Grounding DINO) |
| `segment-anything` | `SamPredictor`, `SamAutomaticMaskGenerator` |
| SAM 2 | Video SAM, memory attention |
| EfficientSAM | Distilled SAM, ~20× faster |
| Mobile SAM | Lightweight for edge |
| Grounded-SAM | Grounding DINO + SAM pipeline |
| Applications | Medical, satellite, interactive editing |

---

#### Lesson 04.05 — Video Object Segmentation
**File**: `_12_04_05_video_object_segmentation.md`

| Topics | Subtopics |
|---|---|
| Semi-supervised VOS | First frame + mask propagation |
| STM | Space-Time Memory network |
| XMem | Long-term memory for VOS |
| SAM 2 for video | Object-level tracking + segmentation |
| Unsupervised VOS | Saliency-based motion segmentation |
| DAVIS benchmark | Evaluation protocol, J&F metric |

---

#### Lesson 04.06 — Medical Image Segmentation
**File**: `_12_04_06_medical_image_segmentation.md`

| Topics | Subtopics |
|---|---|
| 2D vs 3D segmentation | Slice-by-slice vs volumetric |
| nnU-Net | Self-configuring framework, SOTA baseline |
| Swin UNETR | Hybrid Transformer for 3D medical |
| MONAI framework | Medical transforms, sliding window, metrics |
| Loss functions | Dice, Tversky, Dice+BCE combo |
| Datasets | BraTS, BTCV, Decathlon, ISIC |
| Evaluation | Dice, HD95, NSD |

---

#### Lesson 04.07 — Satellite and Remote Sensing Segmentation
**File**: `_12_04_07_satellite_remote_sensing_segmentation.md`

| Topics | Subtopics |
|---|---|
| Multi-spectral imagery | RGB + NIR + SWIR channels |
| GSD resolution | Sub-meter to 30m, impact on model choice |
| ChangeFormer | Change detection Transformer |
| U-Net for satellite | Skip connections for fine structures |
| `torchgeo` | Geospatial datasets and transforms |
| Datasets | SpaceNet, iSAID, ISPRS Potsdam |
| Evaluation | IoU, F1, building footprint metrics |

---

#### Lesson 04.08 — Depth Estimation and Scene Reconstruction
**File**: `_12_04_08_depth_estimation_scene_reconstruction.md`

| Topics | Subtopics |
|---|---|
| Monocular depth | DPT, Depth Anything, Marigold |
| Stereo depth | SGM, PSMNet, CFNet |
| `Depth Anything v2` | Foundation depth model |
| 3D reconstruction | MVS, NeRF, Gaussian Splatting |
| NeRF | Neural Radiance Fields |
| 3D Gaussian Splatting | Fast rendering, explicit 3D representation |
| SLAM | Simultaneous Localization And Mapping |
| Point cloud from depth | `Open3D` library |

---

## MODULE 05 — OCR and Document Understanding

**Folder**: `_12_05_ocr_and_document_understanding/`  
**Lesson Count**: 7  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Text Detection in Images
**File**: `_12_05_01_text_detection_in_images.md`

| Topics | Subtopics |
|---|---|
| Text detection vs OCR | Localization vs recognition |
| EAST | Efficient and Accurate Scene Text |
| DBNet | Differentiable binarization |
| PAN | Pixel Aggregation Network |
| `PaddleOCR` detection | DB, SAST modules |
| Curved text | Arbitrary-shape text detection |
| TextSpotter | End-to-end detect + recognize |

---

#### Lesson 05.02 — Text Recognition (OCR)
**File**: `_12_05_02_text_recognition_ocr.md`

| Topics | Subtopics |
|---|---|
| CRNN | CNN + BiLSTM + CTC |
| CTC loss | Connectionist Temporal Classification |
| Attention-based OCR | SAR, SATRN |
| ViT-based OCR | TrOCR, SVTR |
| `PaddleOCR` recognition | PP-OCRv4, multi-language |
| `EasyOCR` | Simple multi-language wrapper |
| `Tesseract` | Traditional OCR engine |
| Evaluation | Character accuracy, word accuracy, NED |

---

#### Lesson 05.03 — End-to-End OCR Systems
**File**: `_12_05_03_end_to_end_ocr_systems.md`

| Topics | Subtopics |
|---|---|
| PaddleOCR full pipeline | Detection → Cls → Recognition |
| `surya` | Modern transformer-based OCR |
| `doctr` | Document text recognition toolkit |
| Language correction | Beam search + language model |
| Multi-orientation | 0°, 90°, 180°, 270° handling |
| GPU batch inference | Speed optimization |

---

#### Lesson 05.04 — Document Layout Analysis
**File**: `_12_05_04_document_layout_analysis.md`

| Topics | Subtopics |
|---|---|
| Layout detection | Title, paragraph, table, figure, list |
| DiT | Document Image Transformer |
| LayoutLM v3 | Text + layout + image joint model |
| `layoutparser` | Detectron2-based layout parser |
| Table detection | TableNet, CascadeTabNet |
| PDF parsing | `pdfplumber`, `pymupdf`, `camelot` |
| DocBank dataset | Layout understanding benchmark |

---

#### Lesson 05.05 — Table Extraction and Structured Data
**File**: `_12_05_05_table_extraction_structured_data.md`

| Topics | Subtopics |
|---|---|
| Table structure recognition | Row, column, cell boundary |
| TATR | Table Transformer |
| `table-transformer` | HuggingFace table model |
| Cell content extraction | OCR within cells |
| `img2table` | Automatic table extraction |
| Evaluation | TEDS metric |
| Output formats | CSV, JSON, markdown tables |

---

#### Lesson 05.06 — Handwriting Recognition
**File**: `_12_05_06_handwriting_recognition.md`

| Topics | Subtopics |
|---|---|
| Online vs offline HWR | Pen strokes vs static image |
| IAM dataset | English handwriting benchmark |
| TrOCR for handwriting | Fine-tuned transformer |
| IAM lines vs words | Segmentation-based vs line-level |
| Math expression recognition | IM2LaTeX, CROHME dataset |
| Evaluation | CER, WER |

---

#### Lesson 05.07 — Visual Document Intelligence
**File**: `_12_05_07_visual_document_intelligence.md`

| Topics | Subtopics |
|---|---|
| Document AI | Form understanding, key-value extraction |
| LayoutLMv3 | Joint text + image + layout |
| Donut | OCR-free document understanding |
| DocVQA | Visual question answering on documents |
| Invoice / receipt processing | KIE (Key Information Extraction) |
| `transformers` DocVQA models | HuggingFace pipeline |
| Business applications | IDP, intelligent document processing |

---

## MODULE 06 — Face Recognition and Biometrics

**Folder**: `_12_06_face_recognition_and_biometrics/`  
**Lesson Count**: 7  
**Learning Order**: 6th

### Lessons

#### Lesson 06.01 — Face Detection
**File**: `_12_06_01_face_detection.md`

| Topics | Subtopics |
|---|---|
| Viola-Jones | Haar cascade (classical, fast) |
| MTCNN | Multi-task cascade CNN, landmarks |
| RetinaFace | Feature pyramid, joint detection + alignment |
| SCRFD | Sample & Computation Redistribution |
| `insightface` | `app.FaceAnalysis`, detection + recognition |
| `mediapipe.face_detection` | Real-time mobile detection |
| Evaluation | WiderFace benchmark, AP |

---

#### Lesson 06.02 — Face Alignment and Preprocessing
**File**: `_12_06_02_face_alignment_preprocessing.md`

| Topics | Subtopics |
|---|---|
| Face landmarks | 5-point, 68-point, 478-point |
| `dlib` landmark predictor | 68 landmarks |
| `mediapipe.face_mesh` | 478 landmarks real-time |
| Affine alignment | Eyes alignment to fixed positions |
| Cropping strategy | 112×112, 160×160 aligned crops |
| Quality filtering | Blur, occlusion, extreme pose |
| Face anti-spoofing (intro) | Liveness detection |

---

#### Lesson 06.03 — Face Recognition and Verification
**File**: `_12_06_03_face_recognition_verification.md`

| Topics | Subtopics |
|---|---|
| ArcFace | Additive angular margin, `insightface` |
| CosFace | Large margin cosine loss |
| ElasticFace | Elastic margin loss |
| AdaFace | Image quality-aware margin |
| FaceNet | Triplet loss, Google architecture |
| Embedding extraction | 512-dim, L2-normalized |
| Threshold selection | FAR/FRR tradeoff, EER |
| LFW / IJB-C / AgeDB | Benchmark protocols |

---

#### Lesson 06.04 — Person Re-Identification
**File**: `_12_06_04_person_re_identification.md`

| Topics | Subtopics |
|---|---|
| ReID definition | Matching person across cameras |
| Market-1501 / DukeMTMC | Standard ReID benchmarks |
| Part-based models | PCB, MGN |
| Transformer ReID | TransReID |
| Occluded ReID | Keypoint-based alignment |
| Query-gallery matching | Rank-1, mAP evaluation |
| `torchreid` | Unified ReID framework |

---

#### Lesson 06.05 — Facial Attribute Analysis
**File**: `_12_06_05_facial_attribute_analysis.md`

| Topics | Subtopics |
|---|---|
| Age estimation | Ordinal regression, DLDL |
| Gender classification | Binary + multi-gender formulations |
| Emotion recognition | AffectNet, RAF-DB datasets |
| Attribute prediction | CelebA 40 attributes |
| Face parsing | Hair, skin, eyes, lips segmentation |
| BiSeNet for face parsing | Region-level face analysis |

---

#### Lesson 06.06 — Face Generation and Manipulation
**File**: `_12_06_06_face_generation_manipulation.md`

| Topics | Subtopics |
|---|---|
| StyleGAN2/3 | High-quality face synthesis |
| Face swapping | SimSwap, GHOST |
| Face reenactment | FOMM, LIA |
| Deepfake detection | FaceForensics++, DFDC datasets |
| Detection models | Xception, EfficientNet classifier |
| Ethical considerations | Consent, watermarking, C2PA |

---

#### Lesson 06.07 — Biometric Systems Engineering
**File**: `_12_06_07_biometric_systems_engineering.md`

| Topics | Subtopics |
|---|---|
| Biometric pipeline | Capture → Quality → Feature → Match → Decision |
| ISO/IEC standards | ISO 30107 PAD, ISO 19794 templates |
| Multi-modal biometrics | Face + fingerprint + iris fusion |
| Anti-spoofing | 3DDFA, DepthFAS, rPPG liveness |
| FIDO2 / WebAuthn | Biometric authentication standard |
| Privacy regulations | GDPR Art.9, BIPA (Illinois) |
| Forensic applications | Face age progression |

---

## MODULE 07 — 3D Vision and Point Clouds

**Folder**: `_12_07_3d_vision_and_point_clouds/`  
**Lesson Count**: 6  
**Learning Order**: 7th

### Lessons

#### Lesson 07.01 — Point Cloud Fundamentals
**File**: `_12_07_01_point_cloud_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Point cloud representation | (x,y,z) + intensity + RGB |
| LiDAR sensor | Time-of-flight, scan pattern, ROS bags |
| Depth camera | Intel RealSense, Azure Kinect, ToF |
| `Open3D` | `read_point_cloud`, `visualize`, `voxel_down_sample` |
| PCL (Point Cloud Library) | C++/Python interface |
| KD-tree / Octree | Spatial indexing for point clouds |
| Ground removal | RANSAC plane fitting |

---

#### Lesson 07.02 — Point Cloud Deep Learning
**File**: `_12_07_02_point_cloud_deep_learning.md`

| Topics | Subtopics |
|---|---|
| PointNet | Permutation-invariant, global features |
| PointNet++ | Hierarchical local feature learning |
| DGCNN | Dynamic graph CNN, EdgeConv |
| PointTransformer | Self-attention on point clouds |
| `torch-points3d` | Unified point cloud framework |
| Tasks | Classification, part segmentation, semantic seg |
| ModelNet40 / ShapeNet | Standard benchmarks |

---

#### Lesson 07.03 — Neural Radiance Fields (NeRF)
**File**: `_12_07_03_neural_radiance_fields_nerf.md`

| Topics | Subtopics |
|---|---|
| NeRF formulation | Continuous 5D function, volume rendering |
| Positional encoding | Fourier features for high-frequency |
| Hierarchical sampling | Coarse + fine network |
| Instant-NGP | Hash encoding, real-time NeRF |
| Mip-NeRF 360 | Unbounded scenes |
| `nerfstudio` | Modular NeRF training framework |
| Applications | Novel view synthesis, scene editing |

---

#### Lesson 07.04 — 3D Gaussian Splatting
**File**: `_12_07_04_3d_gaussian_splatting.md`

| Topics | Subtopics |
|---|---|
| 3DGS formulation | Explicit 3D Gaussians, alpha compositing |
| Initialization | SfM point cloud from COLMAP |
| Optimization | Adaptive density control, opacity pruning |
| Rasterization | Tile-based differentiable rasterizer |
| `gaussian-splatting` | Official implementation |
| `gsplat` | Nerfstudio-compatible library |
| Speed comparison | 3DGS vs NeRF rendering speed |
| 4D Gaussian Splatting | Dynamic scene extension |

---

#### Lesson 07.05 — Stereo Vision and Depth
**File**: `_12_07_05_stereo_vision_depth.md`

| Topics | Subtopics |
|---|---|
| Stereo geometry | Epipolar lines, rectification |
| Semi-Global Matching | SGM algorithm |
| Deep stereo | PSMNet, CFNet, GANet |
| RAFT-Stereo | Optical flow-based stereo |
| Disparity to depth | Baseline × focal / disparity |
| RGB-D cameras | Intel RealSense, structured light |
| Point cloud from stereo | Reprojection, `cv2.reprojectImageTo3D` |

---

#### Lesson 07.06 — SLAM and Localization
**File**: `_12_07_06_slam_and_localization.md`

| Topics | Subtopics |
|---|---|
| SLAM overview | Mapping + localization simultaneously |
| ORB-SLAM3 | Visual-inertial SLAM |
| LIO-SAM | LiDAR-IMU odometry |
| Visual odometry | Monocular, stereo, RGB-D |
| Loop closure | Bag-of-Words, NetVLAD |
| RTAB-Map | Real-time appearance-based SLAM |
| ROS2 integration | Nav2, map server, AMCL |

---

## MODULE 08 — Vision-Language Models

**Folder**: `_12_08_vision_language_models/`  
**Lesson Count**: 8  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — CLIP and Zero-Shot Vision
**File**: `_12_08_01_clip_zero_shot_vision.md`

| Topics | Subtopics |
|---|---|
| CLIP architecture | Dual encoder: image + text |
| Contrastive pretraining | 400M image-text pairs |
| Zero-shot classification | Text templates, prompt engineering |
| `open_clip` | `create_model_and_transforms`, `tokenize` |
| CLIP embeddings | Cosine similarity search |
| Fine-tuning CLIP | LoRA, CLIP-Adapter |
| Evaluation | ImageNet zero-shot: 76.2% top-1 |
| Applications | Image search, content moderation, tagging |

---

#### Lesson 08.02 — Image Captioning
**File**: `_12_08_02_image_captioning.md`

| Topics | Subtopics |
|---|---|
| CNN + RNN captioning | Show and Tell |
| Attention-based captioning | Show, Attend and Tell |
| BLIP | Bootstrapped Language-Image Pre-training |
| BLIP-2 | Frozen LLM + Q-Former |
| `transformers.BlipForConditionalGeneration` | HuggingFace BLIP |
| Evaluation | CIDEr, BLEU, METEOR, SPICE |
| COCO Captions / NoCaps | Benchmark datasets |

---

#### Lesson 08.03 — Visual Question Answering
**File**: `_12_08_03_visual_question_answering.md`

| Topics | Subtopics |
|---|---|
| VQA task | Image + question → answer |
| ViLBERT | Dual-stream vision-language BERT |
| OSCAR | Anchor point object tags |
| BLIP-2 VQA | Frozen image encoder + LLM |
| GQA / VQAv2 datasets | Benchmark protocols |
| Open-ended vs MC | Generative vs classification head |
| VQA evaluation | Accuracy, soft scoring |

---

#### Lesson 08.04 — Grounding and Referring Expression
**File**: `_12_08_04_grounding_referring_expression.md`

| Topics | Subtopics |
|---|---|
| Visual grounding | "Find the red chair on the left" |
| Grounding DINO | Open-vocabulary detection |
| GLIP | Grounded Language-Image Pre-training |
| REC / REG | Referring Expression Comprehension / Generation |
| RefCOCO datasets | RefCOCO, RefCOCO+, RefCOCOg |
| Phrase grounding | Token-region alignment |

---

#### Lesson 08.05 — Large Vision-Language Models (LVLMs)
**File**: `_12_08_05_large_vision_language_models.md`

| Topics | Subtopics |
|---|---|
| LLaVA | Visual instruction tuning, LLaMA + CLIP |
| LLaVA-1.5 / LLaVA-NeXT | Improved visual encoder, multi-image |
| InternVL | Strong open-source LVLM |
| Qwen-VL | Alibaba multimodal |
| Phi-3.5-vision | Small efficient LVLM |
| MiniCPM-V | Efficient Chinese LVLM |
| `transformers.LlavaForConditionalGeneration` | HuggingFace interface |
| Tasks | VQA, captioning, chart reading, grounding |

---

#### Lesson 08.06 — Vision-Language for Detection and Segmentation
**File**: `_12_08_06_vision_language_detection_segmentation.md`

| Topics | Subtopics |
|---|---|
| Open-vocabulary detection | Detect any category by name |
| Grounding DINO | Text → bounding boxes |
| GLIP / GLIPv2 | Phrase grounding |
| OWL-ViT | Transferable open-vocabulary detection |
| SEEM | Segment Everything Everywhere Multi-Modal |
| Open-vocabulary segmentation | FC-CLIP, ODISE |

---

#### Lesson 08.07 — Chart and Diagram Understanding
**File**: `_12_08_07_chart_diagram_understanding.md`

| Topics | Subtopics |
|---|---|
| Chart types | Bar, line, scatter, pie, heatmap |
| ChartQA dataset | Chart visual question answering |
| UniChart | Unified chart understanding model |
| MatCha | Math reasoning on charts |
| `DePlot` | Chart to table conversion |
| Table QA | ChartToTable → TaPas / OmniTab |

---

#### Lesson 08.08 — Multimodal Embeddings and Search
**File**: `_12_08_08_multimodal_embeddings_search.md`

| Topics | Subtopics |
|---|---|
| Shared embedding space | Images and text in same vector space |
| `imagebind` | Six modalities in one embedding |
| FAISS multimodal | Cross-modal nearest neighbor |
| `clip-retrieval` | Billion-scale CLIP search |
| Vector databases | Pinecone, Weaviate, Qdrant for CV |
| Product image search | E-commerce multimodal retrieval |
| Content-based image retrieval | CBIR at scale |

---

## MODULE 09 — Domain-Specific Computer Vision

**Folder**: `_12_09_domain_specific_cv/`  
**Lesson Count**: 7  
**Learning Order**: 9th

### Lessons

#### Lesson 09.01 — Medical Computer Vision
**File**: `_12_09_01_medical_computer_vision.md`

| Topics | Subtopics |
|---|---|
| Imaging modalities | X-ray, CT, MRI, ultrasound, pathology |
| CheXNet | Pneumonia detection in chest X-rays |
| PathologyAI | Whole-slide image analysis |
| CONCH / UNI | Foundation models for pathology |
| Retinal imaging | Diabetic retinopathy, OCT |
| Regulatory compliance | FDA SaMD, CE marking, IEC 62304 |
| `MONAI` | Medical-specific toolkit |

---

#### Lesson 09.02 — Autonomous Driving Perception
**File**: `_12_09_02_autonomous_driving_perception.md`

| Topics | Subtopics |
|---|---|
| Sensor stack | Camera + LiDAR + Radar + GPS/IMU |
| BEV perception | Bird's Eye View from cameras |
| BEVFusion | Multi-sensor fusion in BEV space |
| Lane detection | CLRNet, LaneATT |
| Traffic sign recognition | German GTSRB |
| nuScenes / Waymo | Large-scale AD benchmarks |
| End-to-end driving | CARLA, Transfuser |

---

#### Lesson 09.03 — Industrial Quality Inspection
**File**: `_12_09_03_industrial_quality_inspection.md`

| Topics | Subtopics |
|---|---|
| Defect classification | Surface defects, PCB inspection |
| Anomaly detection | PatchCore, PaDiM on production line |
| MVTec AD | Benchmark for industrial AD |
| Few-shot defect detection | WinCLIP, SPADE |
| `anomalib` | Production-grade anomaly library |
| 6-DoF pose estimation | BOP benchmark, FoundPose |
| Real-time edge deployment | Jetson + DeepStream |

---

#### Lesson 09.04 — Retail and E-Commerce Vision
**File**: `_12_09_04_retail_ecommerce_vision.md`

| Topics | Subtopics |
|---|---|
| Product recognition | SKU-level classification |
| Visual search | CLIP-based product retrieval |
| Planogram compliance | Shelf detection + product count |
| Try-on AI | Virtual try-on, warping-based |
| Price tag OCR | Text detection + extraction |
| Inventory counting | Detection + tracking |
| Fashion AI | Category, attribute, style prediction |

---

#### Lesson 09.05 — Agricultural and Environmental CV
**File**: `_12_09_05_agricultural_environmental_cv.md`

| Topics | Subtopics |
|---|---|
| Crop disease detection | Plant pathology classification |
| Weed detection | Real-time for precision agriculture |
| UAV/drone imagery | Aerial field mapping |
| NDVI segmentation | Vegetation index from multi-spectral |
| Counting in dense scenes | Crop yield estimation, crowd |
| Species identification | iNaturalist-style classification |

---

#### Lesson 09.06 — Security and Surveillance Vision
**File**: `_12_09_06_security_surveillance_vision.md`

| Topics | Subtopics |
|---|---|
| Multi-camera tracking | Cross-camera ReID |
| Crowd density estimation | CSRNet, BayesianCrowd |
| Action recognition in CCTV | Skeleton-based, video-based |
| Weapon detection | Knife, gun detection datasets |
| License plate recognition | ALPR, LPRNet |
| PPE compliance | Hard hat, vest, mask detection |
| Ethics and privacy | Bias, consent, GDPR compliance |

---

#### Lesson 09.07 — Geospatial and Remote Sensing
**File**: `_12_09_07_geospatial_remote_sensing.md`

| Topics | Subtopics |
|---|---|
| Satellite imagery sources | Sentinel-2, Landsat, Planet, Maxar |
| `torchgeo` | Geospatial deep learning library |
| `rasterio` / `GDAL` | Geospatial raster processing |
| Land cover classification | LoveDA, DeepGlobe datasets |
| Building extraction | SpaceNet challenge |
| Change detection | BitempNet, ChangeFormer |
| Flood / fire mapping | Crisis mapping with satellite data |
| `samgeo` | Segment Anything for geospatial |

---

## MODULE 10 — Industry Projects

**Folder**: `_12_10_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 10th (Capstone)

### Lessons

#### Lesson 10.01 — Real-Time CCTV Analytics System
**File**: `_12_10_01_real_time_cctv_analytics_system.md`

| Topics | Subtopics |
|---|---|
| Pipeline | RTSP → YOLOv8 → ByteTrack → ReID → Alert |
| ByteTrack | Multi-object tracking, SORT++ |
| DeepStream | NVIDIA multi-stream inference |
| Crowd counting | CSRNet integration |
| FastAPI dashboard | WebSocket streaming results |
| Edge deployment | Jetson Orin + TensorRT |

---

#### Lesson 10.02 — Document Intelligence Platform
**File**: `_12_10_02_document_intelligence_platform.md`

| Topics | Subtopics |
|---|---|
| Pipeline | PDF → Layout → OCR → Table → KIE → JSON |
| Tools | `surya` + `table-transformer` + LayoutLMv3 |
| Invoice processing | Key-value extraction, validation |
| API service | FastAPI + async processing |
| Batch processing | Multi-document pipeline |
| Evaluation | End-to-end field extraction accuracy |

---

#### Lesson 10.03 — Face Recognition Attendance System
**File**: `_12_10_03_face_recognition_attendance_system.md`

| Topics | Subtopics |
|---|---|
| Pipeline | Camera → SCRFD → ArcFace → FAISS → DB |
| Registration | Enroll face → store embedding |
| Identification | Query → nearest neighbor → identity |
| Anti-spoofing | Liveness check integration |
| FastAPI endpoint | `/enroll`, `/identify` |
| Database | SQLite / PostgreSQL attendance records |

---

#### Lesson 10.04 — Medical Image Diagnosis System
**File**: `_12_10_04_medical_image_diagnosis_system.md`

| Topics | Subtopics |
|---|---|
| Task | Chest X-ray pneumonia + pleural effusion |
| Dataset | CheXpert, NIH ChestX-ray14 |
| Model | ViT-Base fine-tuned with MONAI |
| Grad-CAM explanation | Radiologist-interpretable saliency |
| DICOM handling | `pydicom`, windowing, HU values |
| Deployment | FastAPI + OHIF viewer integration |
| Regulatory checklist | FDA guidance reference |

---

#### Lesson 10.05 — Visual Search Engine
**File**: `_12_10_05_visual_search_engine.md`

| Topics | Subtopics |
|---|---|
| Pipeline | Image → CLIP embed → FAISS → results |
| Index building | Batch encoding, FAISS IVF+PQ |
| Multi-modal query | Text OR image as query |
| `clip-retrieval` server | CLIP retrieval at billion-scale |
| FastAPI frontend | Search API, top-K results |
| Filtering | Category + price metadata filtering |
| Evaluation | Recall@K, MRR, NDCG |

---

#### Lesson 10.06 — Autonomous Inspection Robot (Capstone)
**File**: `_12_10_06_autonomous_inspection_robot_capstone.md`

| Topics | Subtopics |
|---|---|
| System | Mobile robot + RGB-D + YOLOv8 + NeRF mapping |
| Detection | Real-time defect detection on production line |
| 3D mapping | ORB-SLAM3 + Open3D reconstruction |
| Anomaly scoring | PatchCore live inference |
| ROS2 integration | Navigation, perception, reporting |
| Cloud reporting | FastAPI + MLflow logging |
| Full end-to-end | Robot → detect → alert → report |

---

## Full Folder Structure

```
docs/curriculum/_12_computer_vision/
│
├── _12_01_cv_foundations_and_image_processing/
│   ├── _12_01_01_digital_image_fundamentals.md
│   ├── _12_01_02_image_transformations_filtering.md
│   ├── _12_01_03_feature_detection_and_descriptors.md
│   ├── _12_01_04_image_segmentation_classical.md
│   ├── _12_01_05_optical_flow_motion_analysis.md
│   ├── _12_01_06_camera_models_calibration.md
│   ├── _12_01_07_image_quality_preprocessing.md
│   └── _12_01_08_video_processing_streaming.md
│
├── _12_02_advanced_classification_and_retrieval/
│   ├── _12_02_01_fine_grained_visual_classification.md
│   ├── _12_02_02_image_retrieval_metric_learning.md
│   ├── _12_02_03_hash_based_image_search.md
│   ├── _12_02_04_zero_shot_few_shot_classification.md
│   ├── _12_02_05_image_anomaly_detection.md
│   ├── _12_02_06_scene_classification_understanding.md
│   └── _12_02_07_image_deduplication_clustering.md
│
├── _12_03_advanced_object_detection/
│   ├── _12_03_01_detection_metrics_benchmarks.md
│   ├── _12_03_02_anchor_free_detection.md
│   ├── _12_03_03_yolo_deep_dive.md
│   ├── _12_03_04_transformer_based_detection.md
│   ├── _12_03_05_multi_scale_feature_pyramid_networks.md
│   ├── _12_03_06_3d_object_detection.md
│   ├── _12_03_07_rotated_oriented_object_detection.md
│   └── _12_03_08_real_time_detection_edge.md
│
├── _12_04_advanced_segmentation/
│   ├── _12_04_01_semantic_segmentation_deep_dive.md
│   ├── _12_04_02_instance_segmentation_deep_dive.md
│   ├── _12_04_03_panoptic_segmentation.md
│   ├── _12_04_04_segment_anything_model_sam.md
│   ├── _12_04_05_video_object_segmentation.md
│   ├── _12_04_06_medical_image_segmentation.md
│   ├── _12_04_07_satellite_remote_sensing_segmentation.md
│   └── _12_04_08_depth_estimation_scene_reconstruction.md
│
├── _12_05_ocr_and_document_understanding/
│   ├── _12_05_01_text_detection_in_images.md
│   ├── _12_05_02_text_recognition_ocr.md
│   ├── _12_05_03_end_to_end_ocr_systems.md
│   ├── _12_05_04_document_layout_analysis.md
│   ├── _12_05_05_table_extraction_structured_data.md
│   ├── _12_05_06_handwriting_recognition.md
│   └── _12_05_07_visual_document_intelligence.md
│
├── _12_06_face_recognition_and_biometrics/
│   ├── _12_06_01_face_detection.md
│   ├── _12_06_02_face_alignment_preprocessing.md
│   ├── _12_06_03_face_recognition_verification.md
│   ├── _12_06_04_person_re_identification.md
│   ├── _12_06_05_facial_attribute_analysis.md
│   ├── _12_06_06_face_generation_manipulation.md
│   └── _12_06_07_biometric_systems_engineering.md
│
├── _12_07_3d_vision_and_point_clouds/
│   ├── _12_07_01_point_cloud_fundamentals.md
│   ├── _12_07_02_point_cloud_deep_learning.md
│   ├── _12_07_03_neural_radiance_fields_nerf.md
│   ├── _12_07_04_3d_gaussian_splatting.md
│   ├── _12_07_05_stereo_vision_depth.md
│   └── _12_07_06_slam_and_localization.md
│
├── _12_08_vision_language_models/
│   ├── _12_08_01_clip_zero_shot_vision.md
│   ├── _12_08_02_image_captioning.md
│   ├── _12_08_03_visual_question_answering.md
│   ├── _12_08_04_grounding_referring_expression.md
│   ├── _12_08_05_large_vision_language_models.md
│   ├── _12_08_06_vision_language_detection_segmentation.md
│   ├── _12_08_07_chart_diagram_understanding.md
│   └── _12_08_08_multimodal_embeddings_search.md
│
├── _12_09_domain_specific_cv/
│   ├── _12_09_01_medical_computer_vision.md
│   ├── _12_09_02_autonomous_driving_perception.md
│   ├── _12_09_03_industrial_quality_inspection.md
│   ├── _12_09_04_retail_ecommerce_vision.md
│   ├── _12_09_05_agricultural_environmental_cv.md
│   ├── _12_09_06_security_surveillance_vision.md
│   └── _12_09_07_geospatial_remote_sensing.md
│
└── _12_10_industry_projects/
    ├── _12_10_01_real_time_cctv_analytics_system.md
    ├── _12_10_02_document_intelligence_platform.md
    ├── _12_10_03_face_recognition_attendance_system.md
    ├── _12_10_04_medical_image_diagnosis_system.md
    ├── _12_10_05_visual_search_engine.md
    └── _12_10_06_autonomous_inspection_robot_capstone.md
```

---

## Learning Order

```
01 CV Foundations & Image Processing  (OpenCV, classical methods)
    ↓
02 Advanced Classification & Retrieval  (Fine-grained, metric learning, FAISS)
    ↓
03 Advanced Object Detection  (Anchor-free, YOLO deep dive, Transformers, 3D)
    ↓
04 Advanced Segmentation  (Semantic, Instance, Panoptic, SAM, Medical)
    ↓
05 OCR & Document Understanding  (Text detect, recognize, layout, table, VDI)
    ↓
06 Face Recognition & Biometrics  (Detect, align, recognize, ReID, biometric systems)
    ↓
07 3D Vision & Point Clouds  (PointNet, NeRF, 3DGS, Stereo, SLAM)
    ↓
08 Vision-Language Models  (CLIP, Captioning, VQA, LLaVA, Grounding)
    ↓
09 Domain-Specific CV  (Medical, Autonomous, Industrial, Retail, Geo)
    ↓
10 Industry Projects (Capstone)
```

---

## Summary Statistics

| Module | Title | Lessons |
|---|---|---|
| 01 | CV Foundations & Image Processing | 8 |
| 02 | Advanced Classification & Retrieval | 7 |
| 03 | Advanced Object Detection | 8 |
| 04 | Advanced Segmentation | 8 |
| 05 | OCR & Document Understanding | 7 |
| 06 | Face Recognition & Biometrics | 7 |
| 07 | 3D Vision & Point Clouds | 6 |
| 08 | Vision-Language Models | 8 |
| 09 | Domain-Specific CV | 7 |
| 10 | Industry Projects | 6 |
| **TOTAL** | | **72 lessons** |

---

## Phase 4 Handoff (NLP)

Nodes introduced in Phase 3 and extended in Phase 4:
- CLIP text encoder → full text embedding models
- LLaVA / VQA → multimodal LLMs
- Document intelligence → full NLP pipeline
- OCR text → NLP downstream tasks (NER, classification)
