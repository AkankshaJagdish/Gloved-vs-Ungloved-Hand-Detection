import os
import json
import cv2
import argparse
from ultralytics import YOLO
from tqdm import tqdm


# ---------------- CLI ----------------

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", default="input_images")
parser.add_argument("--output", default="output")
parser.add_argument("--confidence", type=float, default=0.3)
parser.add_argument("--model", default="model/best.pt")

args = parser.parse_args()

INPUT_DIR = args.input
OUTPUT_DIR = args.output
CONF = args.confidence
MODEL_PATH = args.model


# ---------------- PATH SETUP ----------------

LOG_DIR = "logs"
model = YOLO(MODEL_PATH)

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)


# ---------------- LOAD MODEL ----------------

model = YOLO(MODEL_PATH)


# ---------------- DETECTION LOOP ----------------

for img_name in tqdm(os.listdir(INPUT_DIR)):

    if not img_name.endswith(".jpg"):
        continue

    img_path = os.path.join(INPUT_DIR, img_name)

    results = model(img_path)[0]

    image = cv2.imread(img_path)

    detections = []

    for box in results.boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        conf = float(box.conf[0])

        if conf < CONF:
            continue

        cls = int(box.cls[0])

        label = model.names[cls]

        detections.append({
            "label": label,
            "confidence": conf,
            "bbox": [x1, y1, x2, y2]
        })

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            f"{label} {conf:.2f}",
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1
        )


    # save image

    cv2.imwrite(
        os.path.join(OUTPUT_DIR, img_name),
        image
    )


    # save json

    log = {
        "filename": img_name,
        "detections": detections
    }

    with open(
        os.path.join(LOG_DIR, img_name.replace(".jpg", ".json")),
        "w"
    ) as f:
        json.dump(log, f, indent=2)