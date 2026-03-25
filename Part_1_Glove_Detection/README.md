# Dataset:
Roboflow PPE Gloves Dataset 

Link: https://universe.roboflow.com/glove-uylxg/glove-q7czq

# Model:
YOLOv8n fine-tuned for 10 epochs

# Pipeline:
1. Load model
2. Run detection
3. Save annotated images
4. Save JSON logs

# Preprocessing:
Used YOLO default augmentations

# Challenges:
- Small hands
- motion blur
- glove colors similar to skin

# How to run:

cd Part_1_Glove_Detection

python detection_script.py --input input_images --output output

# To run full pipeline:

cd Part_1_Glove_Detection

bash run.sh

or (Windows)

cd Part_1_Glove_Detection

run.bat

# To retrain model from scratch:

cd Part_1_Glove_Detection

python train_model.py


# Arguments:

--input       Input folder of images
--output      Output folder for annotated images
--confidence  Confidence threshold
--model       Path to YOLO model

Example:

python detection_script.py --model model/best.pt --input input_images --output output