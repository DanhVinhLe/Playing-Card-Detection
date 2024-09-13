import cv2
import supervision as sv
from ultralytics import YOLO
import numpy as np

class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.card_id = {0: '10C', 1: '10D', 2: '10H', 3: '10S', 4: '2C', 5: '2D', 6: '2H',7: '2S',8: '3C',9: '3D',10: '3H',11: '3S',
                        12: '4C', 13: '4D', 14: '4H', 15: '4S', 16: '5C', 17: '5D', 18: '5H', 19: '5S', 20: '6C', 21: '6D', 22: '6H',
                        23: '6S', 24: '7C', 25: '7D', 26: '7H', 27: '7S', 28: '8C', 29: '8D', 30: '8H', 31: '8S', 32: '9C', 33: '9D',
                        34: '9H', 35: '9S', 36: 'AC', 37: 'AD', 38: 'AH', 39: 'AS', 40: 'JC', 41: 'JD', 42: 'JH', 43: 'JS', 44: 'KC',
                        45: 'KD', 46: 'KH', 47: 'KS', 48: 'QC', 49: 'QD', 50: 'QH', 51: 'QS'}
        self.card_id_inv = {v:k for k,v in self.card_id.items()}
        self.tracker = sv.ByteTrack()
    def detect(self, frame):
        result = self.model.predict(frame, conf = 0.5)
        detection_sv = sv.Detections.from_ultralytics(result[0])
        object_class = []
        bbox = []
        for _, object in enumerate(detection_sv):
            object_cls = object[3]
            object_class.append(object_cls)
            obj_bbox = object[0]
            bbox.append(obj_bbox)
        
        return object_class, bbox
    
    def draw_annotation(self, frame):
        object_class, bbox = self.detect(frame)
        card_class = [self.card_id[i] for i in object_class]
        for i in range(len(object_class)):
            cv2.rectangle(frame, (int(bbox[i][0]), int(bbox[i][1])), (int(bbox[i][2]), int(bbox[i][3])), color= (0,0,255), thickness= 2,
                          lineType= cv2.LINE_4)
            cv2.putText(frame, card_class[i], (int(bbox[i][0]), int(bbox[i][1])-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale= 0.6, color= (0,0,255), thickness= 2)
            
        return frame
            

        
    