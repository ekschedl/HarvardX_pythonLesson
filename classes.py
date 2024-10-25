class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p = Point(2, 8)
print(p)        #  Point(2, 8)
print(p.x)     # x: 2
print(p.y)     # y: 8


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        # Исправляем вызов метода open_seats()
        if self.open_seats() == 0:  # Используем self для вызова метода
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Olga", "Elene", "Petja"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
