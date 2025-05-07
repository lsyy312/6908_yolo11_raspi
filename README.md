# 6908_yolo11_raspi
Final project for ELEN6908
# Real-Time YOLOv11 Object Detection on Raspberry Pi 5

##  Overview
Deploying YOLOv11n on Raspberry Pi 5 using NCNN for real-time object detection.

##  Features
- Training on COCO8, COCO128 and Pascal VOC
- Model benchmarking (YOLOv11n vs YOLOv11s, 10 model formats)
- Input size ablation experiments (320/416/512/640)
- NCNN deployment with Pi Camera Module 3

##  How to Run
1. Clone this repo
2. Install dependencies
3. Export model to NCNN
4. Run "yolo predict model='yolo11n_ncnn_model' source=xxxx"


##  Benchmark Summary
| Model                    | mAP\@50-95 | FPS       | Size        |
| ------------------------ | ---------- | --------- | ----------- |
| YOLOv11n (PyTorch)       | 0.6453     | 2.73      | 5.2 MB      |
| YOLOv11n (TorchScript)   | 0.6433     | 2.24      | 10.4 MB     |
| YOLOv11n (ONNX)          | 0.6433     | 5.28      | 10.1 MB     |
| YOLOv11n (OpenVINO)      | 0.6429     | 12.57     | 10.3 MB     |
| YOLOv11n (TF SavedModel) | 0.6433     | 3.36      | 26.2 MB     |
| YOLOv11n (TF GraphDef)   | 0.6433     | 3.40      | 10.2 MB     |
| YOLOv11n (TFLite)        | 0.6433     | 3.20      | 10.2 MB     |
| YOLOv11n (Paddle)        | 0.6433     | 2.22      | 20.2 MB     |
| YOLOv11n (MNN)           | 0.6431     | 8.93      | 10.0 MB     |
| **YOLOv11n (NCNN)**      | **0.6427** | **12.33** | **10.0 MB** |
| YOLOv11s (PyTorch)       | 0.6926     | 1.03     | 18.3 MB     |
| YOLOv11s (TorchScript)   | 0.6851     | 0.84     | 36.4 MB     |
| YOLOv11s (ONNX)          | 0.6851     | 2.15     | 36.2 MB     |
| YOLOv11s (OpenVINO)      | 0.6851     | 5.55     | 36.3 MB     |
| YOLOv11s (TF SavedModel) | 0.6851     | 1.47     | 91.8 MB     |
| YOLOv11s (TF GraphDef)   | 0.6851     | 1.61     | 36.3 MB     |
| YOLOv11s (TFLite)        | 0.6851     | 1.15     | 36.3 MB     |
| YOLOv11s (Paddle)        | 0.6851     | 0.89     | 72.4 MB     |
| YOLOv11s (MNN)           | 0.6857     | 3.71     | 36.1 MB     |
| **YOLOv11s (NCNN)**      | **0.6850** | **4.76** | **36.1 MB** |


## 📄 License
MIT
