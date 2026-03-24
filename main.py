import cv2
from pose_module import PoseDetector
from utils import calculate_angle

cap = cv2.VideoCapture(0)
detector = PoseDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = detector.find_pose(frame)

    try:
        # Landmark IDs: 23=hip, 25=knee, 27=ankle (left side)
        hip = detector.get_landmark(frame, 23)
        knee = detector.get_landmark(frame, 25)
        ankle = detector.get_landmark(frame, 27)

        angle = calculate_angle(hip, knee, ankle)

        # Display angle on screen
        cv2.putText(frame, f'Knee Angle: {angle}',
                    knee,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

    except:
        pass

    cv2.imshow("Knee Angle Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()