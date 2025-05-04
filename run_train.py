from ultralytics import YOLOWorld

model = YOLOWorld('./yolov8x-worldv2.pt')
dataset = './dataset.yaml'
n_epoch = 100
img_size = 640
batch_size = 16
patience = 100
device = '0'
# cache = 'ram'
results = model.train(data=dataset, epochs=n_epoch, imgsz=img_size,
                      batch=batch_size,
                      patience=patience,
                      device=device,
                      save=True,
                      # cache=cache
                      )
