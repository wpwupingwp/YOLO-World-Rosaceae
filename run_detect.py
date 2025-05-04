from ultralytics import YOLOWorld
from pathlib import Path

#model = YOLOWorld('./yolov8x-worldv2.pt')
model = YOLOWorld('./runs/detect/train4/weights/best.pt')
# avolid other labels' influence
model.set_classes('leaf,flower,fruit,stem,root,plant'.split(','))
# set img folder path
img_folder = Path('./tests')
# .jpg or others? (.png, .tiff, .bmp)
for img in img_folder.glob('*.jpg'):
    result = model(img)
    for r in result:
        print(r.summary())
