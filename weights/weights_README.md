# Model Weights Documentation

This document summarizes all exported weight files used in this project.

## yolov11n_COCO8
- **Model:** YOLOv11n
- **Dataset:** COCO8
- **Input Size:** 640
- **Format:** PyTorch (.pt)
- **Epochs:** 100
- **mAP@50:** 0.912
- **mAP@50–95:** 0.649
- **Use Case:** Training verification and benchmark on small dataset


## yolov11n_COCO128
- **Model:** YOLOv11n
- **Dataset:** COCO128
- **Input Size:** 640
- **Format:** PyTorch (.pt)
- **Epochs:** 100
- **mAP@50:** 0.893
- **mAP@50–95:** 0.742
- **Use Case:** Training verification and benchmark on small dataset

## yolov11n_VOC
- **Model:** YOLOv11n
- **Dataset:** Pascal VOC
- **Input Size:** 640
- **Format:** PyTorch (.pt)
- **Epochs:** 100
- **mAP@50:** 0.843
- **mAP@50–95:** 0.645
- **Use Case:** Primary model for deployment

## yolov11s_VOC
- **Model:** YOLOv11s
- **Dataset:** Pascal VOC
- **Input Size:** 640
- **Format:** PyTorch (.pt)
- **Epochs:** 100
- **mAP@50:** 0.872
- **mAP@50–95:** 0.685
- **Use Case:** Comparison model for accuracy vs speed tradeoff

## yolov11n_VOC_ncnn.param / .bin
- **Model:** YOLOv11n
- **Dataset:** Pascal VOC
- **Input Size:** 320, 416, 512, 640
- **Format:** NCNN (.param/.bin)
- **Epochs:** 100
- **mAP@50:** 0.806
- **mAP@50–95:** 0.610
- **Use Case:** Final deployment on Raspberry Pi 5
