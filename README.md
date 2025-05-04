# Install
```bash
mkdir yolo-world
cd yolo-world
# download clean weight without extra config info
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8x-worldv2.pt
# Python 3.11 or newer
python3 -m venv .venv
source .venv/bin/activate
which python3
python3 -m pip install ultralytics
# use net proxy?
python3 -m pip install --no-cache-dir "git+https://github.com/ultralytics/CLIP.git"
```

# Train
1. prepare dataset
2. write dataset.yaml
3. set dataset path in `~/.config/Ultralytics/settings.json`
4. edit run `python3 run_train.py`

# Use
```bash
# edit img folder path
python3 run_detect.py
```
