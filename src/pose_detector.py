import cv2 as cv 
import mediapipe as mp 
import time

class PoseDetector:
    def __init__(self, model_path = 'src/pose_landmarker_lite.task'):
        BaseOptions = mp.tasks.BaseOptions
        PoseLandmarker = mp.tasks.vision.PoseLandmarker
        PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        options = PoseLandmarkerOptions(
            base_options = BaseOptions(model_asset_path= model_path),
            running_mode = VisionRunningMode.VIDEO
        )

        self.landmarker = PoseLandmarker.create_from_options(options)

    def detect(self, frame):
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format= mp.ImageFormat.SRGB, data= rgb_frame)
        timestamp_ms = int(time.time()*1000)

        result = self.landmarker.detect_for_video(mp_image, timestamp_ms)

        return result.pose_landmarks