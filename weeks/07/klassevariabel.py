class Car:

    wheels = 4

    def __init__(self, color: str):
        self.color = color

red_car = Car("red")
black_car = Car("black")
Car.wheels = 3
print(black_car.wheels)