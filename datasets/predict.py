from ultralytics import YOLO

# Load the trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Predict on a batch of images (all images in a directory)
results = model.predict("dataset/test/images", save=True)  # Provide the path to the image folder
