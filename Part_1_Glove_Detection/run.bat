echo Copying model...

mkdir model

copy runs\detect\train\weights\best.pt model\best.pt

echo Running detection...

python detection_script.py --model model\best.pt --input input_images --output output --confidence 0.3

echo Done
pause