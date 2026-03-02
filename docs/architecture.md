# Architecture Overview

This document explains the internal structure of GCS.

---

## High-Level Design

GCS follows a modular pipeline:

Perception → Intent → Control → Feedback

---

## Core Entry Point

main.py

Initializes:

SystemController

Runs main loop.

---

## SystemController

Location:

gesture/core/system.py

Responsibilities:

* Coordinates all modules
* Processes each video frame
* Maintains system state

---

## Perception Layer

Location:

gesture/perception/

Components:

tracker.py

Detects hand landmarks using MediaPipe.

smoothing.py

Reduces jitter.

Improves stability.

---

## Intent Layer

Location:

gesture/intent/

classifier.py

Responsibilities:

* Interprets landmarks
* Determines gesture meaning

Examples:

Move

Click

Scroll

Pause

---

## Control Layer

Location:

gesture/control/

mouse_physics.py

Responsibilities:

* Converts gestures into OS mouse actions

Uses:

PyAutoGUI

---

## UI Layer

Location:

gesture/ui/

hud.py

Displays:

* FPS
* Mode
* Gesture state

---

## Configuration

config.py

Defines:

* Sensitivity
* Speed
* Thresholds

---

## Model

hand_landmarker.task

Provides:

Hand tracking model.

Used by MediaPipe.

---

## Data Flow Diagram

Camera Frame

↓

Tracker

↓

Classifier

↓

Mouse Controller

↓

HUD

---

## Design Goals

* Modular
* Extensible
* Real-time performance
* Easy contribution
