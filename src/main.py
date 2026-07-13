import cv2 as cv
from pose_detector import PoseDetector
from angle_utils import calculate_angle
from rep_counter import RepCounter

cap = cv.VideoCapture(0)
detector = PoseDetector()
counter = RepCounter()

while True:
    ret , frame = cap.read()
    if not ret:
        break

    landmark = detector.detect(frame)

    if landmark:
        pose = landmark[0]
        shoulder = (pose[11].x, pose[11].y)
        elbow = (pose[13].x, pose[13].y)
        wrist = (pose[15].x, pose[15].y)

        min_visibility = min(pose[11].visibility, pose[13].visibility, pose[15].visibility)

        if min_visibility > 0.5:
            angle = calculate_angle(shoulder, elbow, wrist)
            count = counter.update(angle)
            print(f"Elbow angle: {angle:.1f}, Reps: {count}")
        else:
            print("Arm not clearly visible")

    else:
        print("No Pose detected")

    cv.imshow("Rep Counter", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()