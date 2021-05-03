#self represents object in question
class Point():
    def __init__(self, x, y):
        self.alpha = x
        self.beta = y
p = Point(2, 4)
print(p.alpha)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Joe", "jim", "bob"]
for person in people:
    if flight.add_passenger(person):
        print(f"{person} added successfully")
    else:
        print(f"No available seats for {person}")