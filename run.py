import pytorch 
import os 

"!python train.py --img 640 --batch 16 --epochs 250 --data data/data.yaml --cfg ./models/yolov5s.yaml --weights '' --name yolov5s_results_first  --cache"

#to detect
"python3 detect.py --weights ./best.pt --source 1"


# good working models here 
"new_last.pt working well"

"the last last.pt for the first train of day2 is new_day_last.pt"
"the best.pt for the first train of day2 is new_day5.pt"

"python3 detect.py --weights ./weights/new_day_improved.pt --source 1 --conf 0.8" "pretty good
"


# working well revised
"new_day_last"
"new_day5"

