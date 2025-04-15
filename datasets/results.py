from ultralytics import YOLO

# Load your trained YOLOv8 model
model = YOLO('runs/detect/train2/weights/best.pt')  # Replace with your model's path

# Path to the dataset YAML file
data_yaml = 'data.yaml'  # Replace with the path to your dataset YAML

# Perform evaluation
results = model.val(data=data_yaml)

# Print mAP results
print("Evaluation Results:")
print(f"mAP@0.5: {results.metrics['mAP_0.5']:.4f}")
print(f"mAP@0.75: {results.metrics['mAP_0.75']:.4f}")
print(f"mAP@0.5:0.95: {results.metrics['mAP_0.5:0.95']:.4f}")

# For per-class mAP
print("\nPer-Class mAP Scores:")
for class_name, mAP_score in zip(results.names, results.metrics['mAP_per_class']):
    print(f"{class_name}: {mAP_score:.4f}")
