from ultralytics import YOLO

# Load pretrained model
model = YOLO("runs/detect/train/weights/best.pt")

# Train on your dataset
model.train(data="data.yaml", epochs=150, imgsz=640)
