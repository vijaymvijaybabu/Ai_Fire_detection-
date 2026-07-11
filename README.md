# weights/

Place your custom YOLOv8 model file here:

    weights/fire_smoke.pt

## Training your own model

```bash
pip install ultralytics

# Example training command
yolo detect train \
  data=fire_smoke.yaml \
  model=yolov8n.pt \
  epochs=100 \
  imgsz=640 \
  name=fire_smoke_model
```

## Pre-trained options

- **YOLOv8 fire+smoke models** are available on Roboflow Universe:
  https://universe.roboflow.com/search?q=fire+smoke

Download the `.pt` file and rename it `fire_smoke.pt`.

## Expected class map (default in settings)

| ID | Class |
|----|-------|
| 0  | fire  |
| 1  | smoke |

If your model has a different class order, update `FIRE_CLASS_ID` / `SMOKE_CLASS_ID`
in `detectors/fire_detector.py` and `detectors/smoke_detector.py`.
