from measurement import Measurement


class DisplayDevice:

    def __init__(self, measurement: Measurement):
        self.measurement = measurement

    def display(self):

        print(f"DISPLAY: {self.measurement}")

    def run(self):

        COUNT = 10

        print("Display started")

        for i in range(0, COUNT):

            self.display()

        print("Display stopped")
