# Knee Joint Angle Detection using Computer Vision

A real-time computer vision system that detects and measures knee joint angles using MediaPipe Pose estimation and OpenCV.

## Tech Stack
- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Project Structure

knee-angle-detection/
├── main.py

├── pose_module.py

├── utils.py

├── requirements.txt

└── README.md

## Installation

git clone https://github.com/sinega-data/knee-angle-detection.git
cd knee-angle-detection
pip install -r requirements.txt

## Run

python main.py

## How It Works
1. Webcam captures live video
2. MediaPipe Pose detects hip, knee, and ankle landmarks
3. Vector geometry calculates the angle at the knee joint
4. Angle is displayed in real-time on the video feed

## Landmark IDs Used
| Joint | MediaPipe ID |
|-------|-------------|
| Hip   | 23          |
| Knee  | 25          |
| Ankle | 27          |

## Applications
- Physiotherapy monitoring
- Rehabilitation progress tracking
- Fitness form correction

## Author
Sinega M 
B.TECH AIDS
EGS PILLAY ENGINEERING COLLEGE
—[LinkedIn](https://linkedin.com/in/sinegaaipm)
