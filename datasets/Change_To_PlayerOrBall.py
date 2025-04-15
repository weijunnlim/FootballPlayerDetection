import os

# Folder containing your YOLO label files
label_folder = "dataset/train/labels"  # update this if needed

for filename in os.listdir(label_folder):
    if not filename.endswith(".txt"):
        continue

    filepath = os.path.join(label_folder, filename)
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    updated_lines = []
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        obj_id = int(parts[0])
        
        # Convert obj_id to class_id
        class_id = 0 if 1 <= obj_id <= 22 else 1  # 0 for players, 1 for ball
        rest = parts[1:]  # x_center, y_center, w, h
        updated_lines.append(f"{class_id} {' '.join(rest)}")
    
    # Write back
    with open(filepath, 'w') as f:
        f.write('\n'.join(updated_lines))
