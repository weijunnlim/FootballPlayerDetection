import os
import cv2

# Read the labels from labels.txt (Assume class index starts from 0)
with open('/home/weijunl/2_train-val_1min_after_goal/gt/labels.txt', 'r') as f:
    labels = f.read().splitlines()

# Directory where your images and annotations will be stored
images_dir = '/home/weijunl/Football-Object-Detection/datasets/dataset/val/images'
gt_file = '/home/weijunl/2_train-val_1min_after_goal/gt/gt.txt'

# Create a new folder for YOLO annotations
output_dir = 'yolo_annotations/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the gt.txt file and process each annotation line
with open(gt_file, 'r') as f:
    lines = f.readlines()

for line in lines:
    # Split the line into individual components
    parts = line.split(',')
    
    # Extract values from the line
    image_id = int(parts[0])  # Image ID
    class_id = int(parts[1])  # Class ID (corresponding to labels.txt)
    x1 = float(parts[2])  # Bounding box x1
    y1 = float(parts[3])  # Bounding box y1
    width = float(parts[4])  # Bounding box width
    height = float(parts[5])  # Bounding box height
    
    # The image name (assume the format is 1.jpg, 2.jpg, etc.)
    image_name = f"{image_id:06d}.jpg"   # Adjust the extension based on your actual image files
    
    # Get the image dimensions
    image_path = os.path.join(images_dir, image_name)
    img = cv2.imread(image_path)
    img_height, img_width, _ = img.shape
    
    # Convert bounding box to YOLO format (normalized)
    x_center = (x1 + width / 2) / img_width
    y_center = (y1 + height / 2) / img_height
    width = width / img_width
    height = height / img_height
    
    # Create annotation string in YOLO format
    annotation = f"{class_id} {x_center} {y_center} {width} {height}\n"
    
    # Write to the corresponding image's annotation file
    annotation_file = os.path.join(output_dir, f"{image_id}.txt")
    with open(annotation_file, 'a') as ann_f:
        ann_f.write(annotation)