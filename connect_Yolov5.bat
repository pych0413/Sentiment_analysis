@echo off
CD yolov5
python detect.py --img 416 --weights runs/train/exp3/weights/best.pt --source ../face.jpg