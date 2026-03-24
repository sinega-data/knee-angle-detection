import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.mp_draw = mp.solutions.drawing_utils

    def find_pose(self, frame, draw=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(rgb)
        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(
                frame,
                self.results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )
        return frame

    def get_landmark(self, frame, landmark_id):
        h, w, _ = frame.shape
        lm = self.results.pose_landmarks.landmark[landmark_id]
        return [int(lm.x * w), int(lm.y * h)]