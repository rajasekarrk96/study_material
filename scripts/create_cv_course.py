import os

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_12_computer_vision'

LESSONS = [
    # MOD 01
    ("_12_01_cv_foundations_and_image_processing","_12_01_01_digital_image_fundamentals.md",1,1,"Digital Image Fundamentals","CV Foundations",["rgb","color-spaces","opencv","pillow","uint8","exif"],"beginner"),
    ("_12_01_cv_foundations_and_image_processing","_12_01_02_image_transformations_filtering.md",1,2,"Image Transformations and Filtering","CV Foundations",["geometric-transform","gaussian-filter","morphological","sobel","warpaffine"],"intermediate"),
    ("_12_01_cv_foundations_and_image_processing","_12_01_03_feature_detection_and_descriptors.md",1,3,"Feature Detection and Descriptors","CV Foundations",["sift","orb","brief","harris","flann","homography"],"intermediate"),
    ("_12_01_cv_foundations_and_image_processing","_12_01_04_image_segmentation_classical.md",1,4,"Image Segmentation Classical","CV Foundations",["otsu","watershed","grabcut","superpixels","graph-cuts","mean-shift"],"intermediate"),
    ("_12_01_cv_foundations_and_image_processing","_12_01_05_optical_flow_motion_analysis.md",1,5,"Optical Flow and Motion Analysis","CV Foundations",["farneback","lucas-kanade","background-subtraction","mog2","raft","motion-vectors"],"intermediate"),
    ("_12_01_cv_foundations_and_image_processing","_12_01_06_camera_models_calibration.md",1,6,"Camera Models and Calibration","CV Foundations",["pinhole","intrinsic","distortion","calibration","stereo","extrinsic"],"intermediate"),
    ("_12_01_cv_foundations_and_image_processing","_12_01_07_image_quality_preprocessing.md",1,7,"Image Quality and Preprocessing","CV Foundations",["clahe","denoising","ssim","psnr","phash","normalization"],"intermediate"),
    ("_12_01_cv_foundations_and_image_processing","_12_01_08_video_processing_streaming.md",1,8,"Video Processing and Streaming","CV Foundations",["videocapture","rtsp","decord","torchvision-io","webrtc","frame-extraction"],"intermediate"),
    # MOD 02
    ("_12_02_advanced_classification_and_retrieval","_12_02_01_fine_grained_visual_classification.md",2,1,"Fine-Grained Visual Classification","Classification and Retrieval",["fine-grained","cub-200","bilinear-pooling","cbam","long-tail","ws-dan"],"advanced"),
    ("_12_02_advanced_classification_and_retrieval","_12_02_02_image_retrieval_metric_learning.md",2,2,"Image Retrieval and Metric Learning","Classification and Retrieval",["metric-learning","triplet-loss","arcface","faiss","hnsw","re-ranking"],"advanced"),
    ("_12_02_advanced_classification_and_retrieval","_12_02_03_hash_based_image_search.md",2,3,"Hash-Based Image Search","Classification and Retrieval",["lsh","deep-hashing","product-quantization","ivf","binary-embeddings","billion-scale"],"advanced"),
    ("_12_02_advanced_classification_and_retrieval","_12_02_04_zero_shot_few_shot_classification.md",2,4,"Zero-Shot and Few-Shot Classification","Classification and Retrieval",["clip-zero-shot","open-clip","prototypical-networks","maml","dino-features"],"intermediate"),
    ("_12_02_advanced_classification_and_retrieval","_12_02_05_image_anomaly_detection.md",2,5,"Image Anomaly Detection","Classification and Retrieval",["patchcore","padim","spade","cutpaste","anomalib","mvtec"],"advanced"),
    ("_12_02_advanced_classification_and_retrieval","_12_02_06_scene_classification_understanding.md",2,6,"Scene Classification and Understanding","Classification and Retrieval",["places365","scene-graphs","visual-relationship","attribute-prediction"],"intermediate"),
    ("_12_02_advanced_classification_and_retrieval","_12_02_07_image_deduplication_clustering.md",2,7,"Image Deduplication and Clustering","Classification and Retrieval",["phash","near-duplicate","dec","cleanvision","clip-retrieval","deep-clustering"],"intermediate"),
    # MOD 03
    ("_12_03_advanced_object_detection","_12_03_01_detection_metrics_benchmarks.md",3,1,"Detection Metrics and Benchmarks","Advanced Detection",["iou","giou","diou","ciou","map","coco","nms","wbf","pycocotools"],"intermediate"),
    ("_12_03_advanced_object_detection","_12_03_02_anchor_free_detection.md",3,2,"Anchor-Free Detection","Advanced Detection",["fcos","centernet","cornernet","atss","tood","anchor-free"],"advanced"),
    ("_12_03_advanced_object_detection","_12_03_03_yolo_deep_dive.md",3,3,"YOLO Deep Dive","Advanced Detection",["yolov8","yolov9","yolov10","yolo-nas","rt-detr","ultralytics","c2f"],"intermediate"),
    ("_12_03_advanced_object_detection","_12_03_04_transformer_based_detection.md",3,4,"Transformer-Based Detection","Advanced Detection",["detr","deformable-detr","dino-detr","dab-detr","dn-detr","co-detr"],"advanced"),
    ("_12_03_advanced_object_detection","_12_03_05_multi_scale_feature_pyramid_networks.md",3,5,"Multi-Scale Feature Pyramid Networks","Advanced Detection",["fpn","panet","bifpn","pafpn","nas-fpn","small-object"],"intermediate"),
    ("_12_03_advanced_object_detection","_12_03_06_3d_object_detection.md",3,6,"3D Object Detection","Advanced Detection",["lidar","pointpillars","voxelnet","centerpoint","bevdet","bevfusion","nuscenes"],"advanced"),
    ("_12_03_advanced_object_detection","_12_03_07_rotated_oriented_object_detection.md",3,7,"Rotated and Oriented Object Detection","Advanced Detection",["obb","dota","s2anet","oriented-rcnn","mmrotate","aerial"],"advanced"),
    ("_12_03_advanced_object_detection","_12_03_08_real_time_detection_edge.md",3,8,"Real-Time Detection and Edge Deployment","Advanced Detection",["tensorrt","openvino","hailo","jetson","deepstream","latency","fps"],"advanced"),
    # MOD 04
    ("_12_04_advanced_segmentation","_12_04_01_semantic_segmentation_deep_dive.md",4,1,"Semantic Segmentation Deep Dive","Advanced Segmentation",["deeplabv3","hrnet","segformer","segmenter","mmsegmentation","miou"],"intermediate"),
    ("_12_04_advanced_segmentation","_12_04_02_instance_segmentation_deep_dive.md",4,2,"Instance Segmentation Deep Dive","Advanced Segmentation",["mask-rcnn","solov2","condinst","queryinst","detectron2","efficientSAM"],"intermediate"),
    ("_12_04_advanced_segmentation","_12_04_03_panoptic_segmentation.md",4,3,"Panoptic Segmentation","Advanced Segmentation",["panopticfpn","maskformer","mask2former","k-net","pq-metric","things-stuff"],"advanced"),
    ("_12_04_advanced_segmentation","_12_04_04_segment_anything_model_sam.md",4,4,"Segment Anything Model SAM","Advanced Segmentation",["sam","sam2","efficientSAM","mobile-sam","grounded-sam","prompt-types"],"intermediate"),
    ("_12_04_advanced_segmentation","_12_04_05_video_object_segmentation.md",4,5,"Video Object Segmentation","Advanced Segmentation",["stm","xmem","sam2-video","davis","unsupervised-vos","jf-metric"],"advanced"),
    ("_12_04_advanced_segmentation","_12_04_06_medical_image_segmentation.md",4,6,"Medical Image Segmentation","Advanced Segmentation",["nnunet","swin-unetr","monai","dice-loss","brats","hausdorff"],"advanced"),
    ("_12_04_advanced_segmentation","_12_04_07_satellite_remote_sensing_segmentation.md",4,7,"Satellite Remote Sensing Segmentation","Advanced Segmentation",["torchgeo","changeformer","spacenet","isprs","rasterio","multispectral"],"advanced"),
    ("_12_04_advanced_segmentation","_12_04_08_depth_estimation_scene_reconstruction.md",4,8,"Depth Estimation and Scene Reconstruction","Advanced Segmentation",["dpt","depth-anything","nerf","3dgs","slam","open3d","marigold"],"advanced"),
    # MOD 05
    ("_12_05_ocr_and_document_understanding","_12_05_01_text_detection_in_images.md",5,1,"Text Detection in Images","OCR and Document",["east","dbnet","pan","paddleocr","curved-text","textspotter"],"intermediate"),
    ("_12_05_ocr_and_document_understanding","_12_05_02_text_recognition_ocr.md",5,2,"Text Recognition OCR","OCR and Document",["crnn","ctc","trocr","easyocr","tesseract","svtr","cer","wer"],"intermediate"),
    ("_12_05_ocr_and_document_understanding","_12_05_03_end_to_end_ocr_systems.md",5,3,"End-to-End OCR Systems","OCR and Document",["paddleocr-full","surya","doctr","language-correction","batch-inference"],"intermediate"),
    ("_12_05_ocr_and_document_understanding","_12_05_04_document_layout_analysis.md",5,4,"Document Layout Analysis","OCR and Document",["dit","layoutlm","layoutparser","tabledet","pdfplumber","pymupdf"],"intermediate"),
    ("_12_05_ocr_and_document_understanding","_12_05_05_table_extraction_structured_data.md",5,5,"Table Extraction and Structured Data","OCR and Document",["tatr","table-transformer","img2table","teds","cell-extraction","csv-output"],"intermediate"),
    ("_12_05_ocr_and_document_understanding","_12_05_06_handwriting_recognition.md",5,6,"Handwriting Recognition","OCR and Document",["trocr-handwriting","iam","im2latex","crohme","cer-wer","online-offline"],"advanced"),
    ("_12_05_ocr_and_document_understanding","_12_05_07_visual_document_intelligence.md",5,7,"Visual Document Intelligence","OCR and Document",["layoutlmv3","donut","docvqa","kie","invoice-processing","idp"],"advanced"),
    # MOD 06
    ("_12_06_face_recognition_and_biometrics","_12_06_01_face_detection.md",6,1,"Face Detection","Face Recognition",["viola-jones","mtcnn","retinaface","scrfd","insightface","mediapipe","widerface"],"intermediate"),
    ("_12_06_face_recognition_and_biometrics","_12_06_02_face_alignment_preprocessing.md",6,2,"Face Alignment and Preprocessing","Face Recognition",["landmarks","dlib","mediapipe-mesh","affine-alignment","quality-filtering"],"intermediate"),
    ("_12_06_face_recognition_and_biometrics","_12_06_03_face_recognition_verification.md",6,3,"Face Recognition and Verification","Face Recognition",["arcface","cosface","elasticface","adaface","facenet","embedding","far-frr","lfw"],"intermediate"),
    ("_12_06_face_recognition_and_biometrics","_12_06_04_person_re_identification.md",6,4,"Person Re-Identification","Face Recognition",["reid","transreid","pcb","mgn","market1501","torchreid","rank-1","map"],"advanced"),
    ("_12_06_face_recognition_and_biometrics","_12_06_05_facial_attribute_analysis.md",6,5,"Facial Attribute Analysis","Face Recognition",["age-estimation","emotion-recognition","celeba","bisenet","face-parsing"],"intermediate"),
    ("_12_06_face_recognition_and_biometrics","_12_06_06_face_generation_manipulation.md",6,6,"Face Generation and Manipulation","Face Recognition",["stylegan","simswap","fomm","deepfake-detection","faceforensics","c2pa"],"advanced"),
    ("_12_06_face_recognition_and_biometrics","_12_06_07_biometric_systems_engineering.md",6,7,"Biometric Systems Engineering","Face Recognition",["iso-30107","anti-spoofing","fido2","multi-modal","gdpr","forensic"],"advanced"),
    # MOD 07
    ("_12_07_3d_vision_and_point_clouds","_12_07_01_point_cloud_fundamentals.md",7,1,"Point Cloud Fundamentals","3D Vision",["open3d","lidar","depth-camera","kd-tree","voxel","ground-removal"],"intermediate"),
    ("_12_07_3d_vision_and_point_clouds","_12_07_02_point_cloud_deep_learning.md",7,2,"Point Cloud Deep Learning","3D Vision",["pointnet","pointnet++","dgcnn","pointtransformer","torch-points3d","modelnet"],"advanced"),
    ("_12_07_3d_vision_and_point_clouds","_12_07_03_neural_radiance_fields_nerf.md",7,3,"Neural Radiance Fields NeRF","3D Vision",["nerf","instant-ngp","mip-nerf","nerfstudio","positional-encoding","volume-rendering"],"advanced"),
    ("_12_07_3d_vision_and_point_clouds","_12_07_04_3d_gaussian_splatting.md",7,4,"3D Gaussian Splatting","3D Vision",["3dgs","colmap","gsplat","4dgs","differentiable-rasterizer","gaussian-splatting"],"advanced"),
    ("_12_07_3d_vision_and_point_clouds","_12_07_05_stereo_vision_depth.md",7,5,"Stereo Vision and Depth","3D Vision",["stereo","sgm","psmnet","raft-stereo","disparity","realsense"],"intermediate"),
    ("_12_07_3d_vision_and_point_clouds","_12_07_06_slam_and_localization.md",7,6,"SLAM and Localization","3D Vision",["orb-slam3","lio-sam","visual-odometry","loop-closure","rtab-map","ros2"],"advanced"),
    # MOD 08
    ("_12_08_vision_language_models","_12_08_01_clip_zero_shot_vision.md",8,1,"CLIP and Zero-Shot Vision","Vision-Language Models",["clip","open-clip","zero-shot","text-templates","clip-adapter","lora-clip"],"intermediate"),
    ("_12_08_vision_language_models","_12_08_02_image_captioning.md",8,2,"Image Captioning","Vision-Language Models",["blip","blip-2","show-attend-tell","cider","bleu","nocaps"],"intermediate"),
    ("_12_08_vision_language_models","_12_08_03_visual_question_answering.md",8,3,"Visual Question Answering","Vision-Language Models",["vqa","vilbert","oscar","blip-2-vqa","gqa","vqav2"],"intermediate"),
    ("_12_08_vision_language_models","_12_08_04_grounding_referring_expression.md",8,4,"Grounding and Referring Expression","Vision-Language Models",["grounding-dino","glip","rec","reg","refcoco","phrase-grounding"],"advanced"),
    ("_12_08_vision_language_models","_12_08_05_large_vision_language_models.md",8,5,"Large Vision-Language Models","Vision-Language Models",["llava","internvl","qwen-vl","phi-3-vision","minicpm-v","multimodal-llm"],"advanced"),
    ("_12_08_vision_language_models","_12_08_06_vision_language_detection_segmentation.md",8,6,"Vision-Language for Detection and Segmentation","Vision-Language Models",["grounding-dino","owl-vit","seem","fc-clip","open-vocabulary","odise"],"advanced"),
    ("_12_08_vision_language_models","_12_08_07_chart_diagram_understanding.md",8,7,"Chart and Diagram Understanding","Vision-Language Models",["chartqa","unichart","matcha","deplot","tapas","chart-to-table"],"advanced"),
    ("_12_08_vision_language_models","_12_08_08_multimodal_embeddings_search.md",8,8,"Multimodal Embeddings and Search","Vision-Language Models",["imagebind","faiss-multimodal","clip-retrieval","pinecone","qdrant","cbir"],"advanced"),
    # MOD 09
    ("_12_09_domain_specific_cv","_12_09_01_medical_computer_vision.md",9,1,"Medical Computer Vision","Domain-Specific CV",["chexnet","pathology-ai","conch","uni","retinal","fda-samd","monai"],"advanced"),
    ("_12_09_domain_specific_cv","_12_09_02_autonomous_driving_perception.md",9,2,"Autonomous Driving Perception","Domain-Specific CV",["bev","bevfusion","clrnet","nuscenes","waymo","carla","transfuser"],"advanced"),
    ("_12_09_domain_specific_cv","_12_09_03_industrial_quality_inspection.md",9,3,"Industrial Quality Inspection","Domain-Specific CV",["patchcore","anomalib","mvtec","winclip","6dof-pose","jetson","deepstream"],"advanced"),
    ("_12_09_domain_specific_cv","_12_09_04_retail_ecommerce_vision.md",9,4,"Retail and E-Commerce Vision","Domain-Specific CV",["sku-recognition","visual-search","planogram","virtual-tryon","fashion-ai"],"intermediate"),
    ("_12_09_domain_specific_cv","_12_09_05_agricultural_environmental_cv.md",9,5,"Agricultural and Environmental CV","Domain-Specific CV",["crop-disease","weed-detection","uav","ndvi","species-identification","counting"],"intermediate"),
    ("_12_09_domain_specific_cv","_12_09_06_security_surveillance_vision.md",9,6,"Security and Surveillance Vision","Domain-Specific CV",["multi-camera-tracking","crowd-density","csrnet","alpr","ppe-detection","gdpr"],"advanced"),
    ("_12_09_domain_specific_cv","_12_09_07_geospatial_remote_sensing.md",9,7,"Geospatial and Remote Sensing","Domain-Specific CV",["sentinel-2","torchgeo","rasterio","spacenet","changeformer","samgeo","flood-mapping"],"advanced"),
    # MOD 10
    ("_12_10_industry_projects","_12_10_01_real_time_cctv_analytics_system.md",10,1,"Real-Time CCTV Analytics System","Industry Projects",["rtsp","yolov8","bytetrack","reid","deepstream","jetson","fastapi"],"advanced"),
    ("_12_10_industry_projects","_12_10_02_document_intelligence_platform.md",10,2,"Document Intelligence Platform","Industry Projects",["surya","table-transformer","layoutlmv3","invoice","fastapi","batch-processing"],"advanced"),
    ("_12_10_industry_projects","_12_10_03_face_recognition_attendance_system.md",10,3,"Face Recognition Attendance System","Industry Projects",["scrfd","arcface","faiss","anti-spoofing","fastapi","sqlite"],"advanced"),
    ("_12_10_industry_projects","_12_10_04_medical_image_diagnosis_system.md",10,4,"Medical Image Diagnosis System","Industry Projects",["chexpert","vit-fine-tuning","grad-cam","pydicom","dicom","ohif"],"advanced"),
    ("_12_10_industry_projects","_12_10_05_visual_search_engine.md",10,5,"Visual Search Engine","Industry Projects",["clip","faiss","clip-retrieval","multimodal-query","fastapi","recall-at-k"],"advanced"),
    ("_12_10_industry_projects","_12_10_06_autonomous_inspection_robot_capstone.md",10,6,"Autonomous Inspection Robot Capstone","Industry Projects",["orb-slam3","yolov8","patchcore","ros2","open3d","mlflow","nerf"],"advanced"),
]

created = 0
skipped = 0
for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"12_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"' + t + '"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "Computer Vision"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 3 CV Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1

print(f"\nDONE - Created: {created}  Skipped: {skipped}  Total: {created+skipped}")
