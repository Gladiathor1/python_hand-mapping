# Hand Mapping — Automatic Hand Bounding-Box Labelling

Python scripts that use **MediaPipe Hands** and **OpenCV** to detect hands in images and automatically generate **YOLO-format bounding-box labels** for them. It was built to speed up annotating a hand dataset for training an object detector: instead of drawing boxes by hand, the scripts detect each hand, pad the box slightly, and write the label file.

## Output format

For each image, a `.txt` file with the same name is written, with one line per detected hand:

```
<class> <x_center> <y_center> <width> <height>
```

- `class` — `0` for a **left** hand, `1` for a **right** hand (from MediaPipe's handedness)
- coordinates are normalised to the image size (0–1), as YOLO expects

## Scripts

| Script | Purpose |
| --- | --- |
| `another.py` | Main batch labeller: processes every image in `./JB/<folder>/`, shows each detection, and writes labels to `<folder>_results/` |
| `myother.py` | Variant of the batch labeller that handles the order of left/right detections explicitly for two-hand images |
| `another2.py` | Debug a single image: draws the padded box and all 21 hand landmarks |
| `main.py` | Experiment based on the MediaPipe static-image example, printing handedness and box coordinates |
| `face.py` | Helper that creates an empty `.txt` label file for every image in `./images` |

## Requirements

- Python 3.8+
- `opencv-python`, `mediapipe`, `imutils`, `protobuf`

```bash
pip install opencv-python mediapipe imutils
```

## Usage

1. Put your images in a folder under `JB/`, e.g. `JB/p19_both21/`.
2. Set `my_file_name` at the top of `another.py` (or `myother.py`) to that folder name.
3. Run:

```bash
python another.py
```

Each image is shown with its bounding boxes while it is processed, and the labels are saved to `p19_both21_results/`.

## Notes

- Boxes are padded around the detected landmarks (40 px left/right, 30 px top, 40 px bottom) so the whole hand is included.
- Images in which no hand is detected produce an empty label file.
