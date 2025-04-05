class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    speed = 100
    color = "black"
    def beep(self):
        print("beep")
    def say_speed(self):
        print(self.speed)
    def say_color(self):
        print(self.color)

class Bus(Transport):
    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner
        self.wheels = 6

    def say_owner(self):
        print("владелец " + self.owner)


class Plane(Transport):
    def __init__(self, speed, color, seats):
        super().__init__(speed, color)
        self.seats = seats
        self.wheels = 12

    def say_seats(self):
        print(self.seats)


plane = Plane(500, "white", 80)
plane.say_seats()
plane.say_color()


# bus = Bus(100, "blue", "state")
# bus.say_owner()
# bus.beep()