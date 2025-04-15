# 🏃‍♂️⚽ Player & Ball Detection

This project uses object detection to analyze football match footage, focusing on detecting only two classes:

- `0` – Player  
- `1` – Ball  

The goal is to create a simplified yet effective object detection system for sports analytics.

---

## 📽️ Demo

_(Demo coming soon or to be added here)_

---

## 🚀 Quick Guide

<details>
<summary><strong>Install</strong></summary>

```bash
git clone https://github.com/weijunnlim/Player-Ball-Detection.git
cd Player-Ball-Detection
pip install -r requirements.txt
</details> <details> <summary><strong>Run Inference on Video</strong></summary>

To run the model on a video, run the following command: 
```
python main.py /path/to/video
```
The annotated video will be saved to "Football Object Detection/output" folder

</details>

<details> <summary><strong>Run Inference on Images</strong></summary>
```
cd datasets
python predict.py
```
This will annotate the images inside the datasets folder.

</details>

<details> <summary><strong>Validation Results</strong></summary>
```
python val.py
```
</details>

<details> <summary><strong>Train the Model</strong></summary>
```
python train.py
```
Make sure your dataset is properly annotated in YOLO format before training.
</details>

<details> <summary><strong>mAP50 Scores</strong></summary>
```
python results.py
```
This script displays the mAP@50 scores for both Player and Ball classes.

</details>

# Dataset Annotation

The original dataset contains 24 classes. This project simplifies them into two:

Class 1–22 → Player (0)
Class 23 → Ball (1)
To convert the dataset, run:





