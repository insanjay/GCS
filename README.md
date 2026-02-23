<p align="center">
  <img src="docs/logo.png" alt="GCS Logo" width="200">
</p>

<p align="center">
  <strong><a href="https://github.com/insanjay">Sanjay Kumar</a> - GCS.</strong>
</p>


<p align="center">
  <strong>Touch-free computer control using hand gestures and computer vision.</strong>
</p>

<p align="center">

  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg">
  <img src="https://img.shields.io/github/repo-size/insanjay/GCS">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue">
  <img src="https://img.shields.io/badge/license-MIT-green">

</p>

---

## About

Gesture Control System (GCS) is a Python-based human–computer interaction system that enables cursor control and system input using hand gestures captured through a standard webcam.

It uses computer vision and MediaPipe hand tracking to interpret hand movements and translate them into operating system mouse actions.

This project is designed as:

* a learning resource
* an experimentation platform
* a foundation for gesture-based interfaces

---

## Features

* Cursor movement using index finger
* Left and right click gestures
* Scroll mode using hand gestures
* Pause / safety mode
* Real-time visual feedback (HUD)
* Modular and extensible architecture

---

## Why This Project Exists

Traditional computer interaction relies on physical devices.

This project explores natural interaction using gestures to:

* reduce dependency on hardware input devices
* experiment with computer vision interfaces
* provide a platform for further development and research

---

## Requirements

* Python 3.8 or newer
* Webcam
* Operating System: Windows, Linux, or macOS

---

## Installation

Clone the repository:

```bash
git clone https://github.com/insanjay/GCS.git
cd GCS
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the MediaPipe hand landmarker model:

[Download Link](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task)

Place the file in the project root:

```id="model"
hand_landmarker.task
```

---

## Quick Start

Run the application:

```bash
python main.py
```

Show your hand to the webcam and perform gestures.

---

## Architecture Overview

The system follows a modular pipeline:

```id="pipeline"
SystemController
   │
   ├── Tracker        (hand detection)
   ├── Classifier     (gesture recognition)
   ├── Mouse Control  (system input execution)
   └── HUD            (visual feedback)
```

---

## Project Structure

```id="structure"
GCS/

main.py

gesture/
   core/
      system.py

   perception/
      tracker.py
      smoothing.py

   intent/
      classifier.py

   control/
      mouse_physics.py

   ui/
      hud.py

   config.py

config.py
gesture_recognition.py
requirements.txt
hand_landmarker.task
mouse_control.py
hand_tracking.py
.gitignore
README.md
```

---

## Configuration

System behavior can be adjusted in:

```id="config"
config.py
```

Examples:

* smoothing
* scroll speed
* gesture cooldown

---

## Roadmap

Planned improvements:

* Tracking optimization
* Performance optimization

---

## Contributing

Contributions are welcome.

Please read:

[CONTRIBUTING.md](CONTRIBUTING.MD)

before submitting a pull request.

---

## Coding Style

This project follows the Python PEP 8 style guide.

Recommended tool:

Ruff

---

## Community

Community channels:

Discord: (coming soon)
Slack: (coming soon)

---

## License

This project is licensed under the MIT License.

See <strong><a href="LICENSE">LICENSE</a></strong> for details.

---

## Acknowledgements

This project is based on gesture recognition concepts using:

* MediaPipe
* OpenCV

and was further structured, improved, and maintained as an open-source project.