from detector import Detector
import cv2

class Calculator():
    def __init__(self):
        self.result = {1: 'Lieng', 2: 'Sap'}
        self.card_id = {0: '10C', 1: '10D', 2: '10H', 3: '10S', 4: '2C', 5: '2D', 6: '2H',7: '2S',8: '3C',9: '3D',10: '3H',11: '3S',
                        12: '4C', 13: '4D', 14: '4H', 15: '4S', 16: '5C', 17: '5D', 18: '5H', 19: '5S', 20: '6C', 21: '6D', 22: '6H',
                        23: '6S', 24: '7C', 25: '7D', 26: '7H', 27: '7S', 28: '8C', 29: '8D', 30: '8H', 31: '8S', 32: '9C', 33: '9D',
                        34: '9H', 35: '9S', 36: 'AC', 37: 'AD', 38: 'AH', 39: 'AS', 40: 'JC', 41: 'JD', 42: 'JH', 43: 'JS', 44: 'KC',
                        45: 'KD', 46: 'KH', 47: 'KS', 48: 'QC', 49: 'QD', 50: 'QH', 51: 'QS'}
        self.transfer = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                       '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    def calculate_score(self, object_class):
        list_class = list(set(object_class))
        list_card = [self.card_id[cls] for cls in list_class]
        list_card.sort()
        card_num = [x[:-1] for x in list_card]
        num = [self.transfer[card] for card in card_num]
        num.sort()
        if (card_num[0] == card_num[1] and card_num[1] == card_num[2]):
            return self.result[2]
        elif ((num[0] +1 == num[1] and num[1] +1 == num[2]) or (num[0] == 12 and num[1] == 13 and num[2] == 1)):
            return self.result[1]
        else:
            return (num[0] + num[1] + num[2]) % 10
    
    def draw_result(self, frame, object_class):
        h,w, _ = frame.shape
        list_class = list(set(object_class))
        if len(list_class) > 3 or len(list_class) < 3:
            cv2.putText(frame, "Invalid", (w -100, h - 25), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale= 0.6, color= (0,0,0), thickness= 2)
        else:
            cv2.putText(frame, f'{self.calculate_score(object_class)}',(w -100, h - 25), fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale= 0.6, color= (0,0,0), thickness=2)
        
        return frame