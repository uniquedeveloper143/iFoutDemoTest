from ultralytics import YOLO
import cv2
from collections import Counter


def count_objects(image_path):

  # here I am Loading YOLOv8 nano model that is the pretrained on COCO
  model = YOLO("yolov8n.pt")

  # Here passing the image path for read
  image = cv2.imread(image_path)

  results = model(image)[0]

  # Here it will get the List of detected class IDs
  class_ids = results.boxes.cls.int().tolist()

  # Here I am assigning the COCO class names
  class_names = model.names

  # Here I am counting unique detected classes in dict as Index:Value
  counts = Counter(class_ids)

  objects_details = {}

  # Add detected object counts with names in the dict
  for class_id, count in counts.items():
      objects_details[class_names[class_id]] = count

  return objects_details
