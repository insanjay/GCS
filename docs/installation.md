# Installation Guide

This guide explains how to install and run the Gesture Control System (GCS) on your local machine.

---

## Requirements

Before installing, ensure you have:

* Python 3.8 or newer
* A working webcam
* Git (optional, for cloning)
* Supported OS:

  * Windows

## Note: We need contributors to check if the exact code is supported on MacOS and Linux

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/insanjay/GCS.git
cd GCS
```

Or download and extract the ZIP file.

---

## Step 2: Create Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```
---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:

* OpenCV
* MediaPipe
* NumPy
* PyAutoGUI

---

## Step 4: Download Hand Landmarker Model

[Download Link](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task)

Place it in the project root:

```
GCS/
hand_landmarker.task
```

---

## Step 5: Run the Application

```bash
python main.py
```

If successful, your webcam feed will open and gesture tracking will begin.

---

## Troubleshooting

### Webcam not detected

Ensure:

* Webcam is connected
* No other app is using webcam

---

### Module not found

Reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

## Next Step

Continue to:

[quick-start.md](quick-start.md)

for gesture usage instructions.
