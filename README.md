# Playing Card Detection

## Introduction

I fine-tuned the YOLOv8 model on a [Roboflow dataset](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/4) to develop a model capable of detecting playing cards in real-time using a webcam. Additionaly, I developed a small program that allows the model to calculate scores based on a game called "Liêng", using the card detected.

## Results
I have finetuned on the additional dataset and here is my result on the validation dataset:
|Class|mAP50|mAP50-95|
|---|---|---|
|all|0.995|0.818|

Although, the result on validation dataset were quite good, the model still encountered errors in real-world applications, such as misidentifying certain cards, like 3 and 5, A and 4,...
### Weight of the best model
[Weight](https://drive.google.com/file/d/1jJ0CRzwR0-kNuy-8hIw_khQBxATCnqJo/view?usp=drive_link)
