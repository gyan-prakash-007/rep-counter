class RepCounter :
    def __init__(self, down_threshould=160,up_threshold=50):
        self.down_threshold = down_threshould
        self.up_threshold = up_threshold
        self.state = "down"
        self.count = 0

    def update(self, angle):
        if angle > self.down_threshold:
            if self.state == "up":
                self.count +=1

            self.state = "down"

        elif angle < self.up_threshold :
            self.state = "up"

        return self.count
    
if __name__ == "__main__" :
    counter = RepCounter()


    test_angle = [170, 150, 100, 60, 40, 100, 150, 170]

    for angle in test_angle:
        count = counter.update(angle)
        print(f"Angle: {angle}, State: {counter.state}, Count: {count}")
