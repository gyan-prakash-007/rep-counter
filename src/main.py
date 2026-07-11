import cv2 as cv
from pose_detector import PoseDetector

cap = cv.VideoCapture(0)
detector = PoseDetector()

while True:
    ret , frame = cap.read()
    if not ret:
        break

    landmark = detector.detect(frame)

    if landmark:
        print("pose detected")

    else:
        print("No Pose detected")

    cv.imshow("Rep Counter", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()