import time
from ultralytics import YOLO
import torch
from tabulate import tabulate

model_path = "./weights/best.pt"
model = YOLO(model_path)

# 测试不同输入尺寸
imgsz_list = [320, 416, 512, 640]
results = []

# 推理轮数用于平均
warmup = 3
test_loops = 30

print(f"\n📊 Running benchmark for: {model_path}")
for imgsz in imgsz_list:
    print(f"🔍 Testing imgsz={imgsz}...")

    # 评估精度（VOC.yaml 替换为你的验证集）
    metrics = model.val(data="VOC.yaml", imgsz=imgsz, batch=1, verbose=False, plots=False)
    map50_95 = metrics.box.map  # 0.5:0.95
    map50 = metrics.box.map50

    # 推理时间测试（以 batch=1 为例）
    dummy_input = torch.randn(1, 3, imgsz, imgsz)
    model.predict(dummy_input, imgsz=imgsz)  # warmup

    t0 = time.time()
    for _ in range(test_loops):
        _ = model.predict(dummy_input, imgsz=imgsz, verbose=False)
    dt = (time.time() - t0) / test_loops
    fps = 1.0 / dt
    dt_ms = dt * 1000

    results.append([imgsz, round(map50, 4), round(map50_95, 4), round(dt_ms, 2), round(fps, 2)])

# ✅ 打印漂亮的表格
print("\n✅ imgsz Benchmark Results:")
print(tabulate(results, headers=["imgsz", "mAP50", "mAP50-95", "InferTime (ms)", "FPS"], tablefmt="github"))
