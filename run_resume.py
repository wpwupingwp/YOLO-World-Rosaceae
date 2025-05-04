from ultralytics import YOLOWorld

model = YOLOWorld('./runs/detect/train4/weights/last.pt')
dataset = './dataset.yaml'
n_epoch = 1000
img_size = 640
batch_size = 16
patience = 300
device = '1'
# cache = 'ram'
results = model.train(data=dataset, epochs=n_epoch, imgsz=img_size,
                      batch=batch_size,
                      patience=patience,
                      device=device,
                      save=True,
                      resume=True
                      # cache=cache
                      )
