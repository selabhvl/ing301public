class Car:

    wheels = 4

    def __init__(self, color: str):
        self.color = color

red_car = Car("red")
black_car = Car("black")
Car.wheels = 3
black_car.wheels = 5
print(red_car.wheels)
print(black_car.wheels)