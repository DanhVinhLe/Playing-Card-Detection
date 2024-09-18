from ultralytics import YOLO
import cv2
from calculator import Calculator
from detector import Detector

def main():
    model = YOLO('models/best.pt')
    detector = Detector('models/best.pt')
    calculator = Calculator()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        h, w, _ = frame.shape
        object_class, _ = detector.detect(frame)
        frame = detector.draw_annotation(frame)
        cv2.rectangle(frame, (w - 200, h - 75), (w,h), (255, 255, 255), cv2.FILLED)
        frame = calculator.draw_result(frame, object_class)
        
        cv2.imshow('Card Detection', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
