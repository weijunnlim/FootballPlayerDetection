from ultralytics import YOLO

# Load the pretrained model
model = YOLO("runs/detect/train/weights/best.pt")

# Validate the model after training
metrics = model.val(data="data.yaml")
print(metrics)
