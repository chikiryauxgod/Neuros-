import json
import os 
from ultralytics import YOLO

model = YOLO("yolov8x.pt")
print(model.info())
