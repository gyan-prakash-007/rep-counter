import math

def calculate_angle(shoulder,elbow,wrist):
    angle_wrist = math.atan2(wrist[1]-wrist[1],wrist[0]-elbow[0])
    angle_shoulder = math.atan2(shoulder[1]-elbow[1],shoulder[0]- elbow[0])


    angle = math.degrees(angle_wrist-angle_shoulder)
    angle = abs(angle)

    if angle >180:
        angle = 360 - angle

    return angle

if __name__ == "__main__":
    shoulder =(0,0)
    elbow = (0,1)
    wrist = (1,1)

    result = calculate_angle(shoulder,elbow,wrist)
    print(f"Calculated angle : {result}")
