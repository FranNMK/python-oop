# oop_assignment.py

# ---------------- Assignment 1 ----------------
# Smartphone + GamingPhone

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # percentage

    def call(self, number):
        return f"Calling {number} from {self.model}..."

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"Battery charged to {self.battery}%"

    def use_storage(self, amount):
        if amount <= self.storage:
            self.storage -= amount
            return f"{amount}GB used. Remaining storage: {self.storage}GB"
        else:
            return "Not enough storage!"


class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        if self.battery > 20:
            self.battery -= 20
            return f"Playing {game_name} 🎮 with {self.cooling_system} cooling! Battery: {self.battery}%"
        else:
            return "Battery too low to play games!"


# ---------------- Assignment 2 ----------------
# Polymorphism Challenge

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# ---------------- Test the Code ----------------
if __name__ == "__main__":
    # Test Smartphone
    phone1 = Smartphone("Samsung", "Galaxy S23", 128, 80)
    print(phone1.call("0712345678"))
    print(phone1.use_storage(20))

    # Test GamingPhone
    gaming_phone = GamingPhone("Asus", "ROG Phone 7", 256, 100, "Liquid Cooling")
    print(gaming_phone.play_game("PUBG Mobile"))
    print(gaming_phone.charge(15))

    # Test Vehicles
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
