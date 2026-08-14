class CeilingFan:
    def __init__(self, room: str, speed: int = 0) -> None:
        self.room = room
        self.speed = speed

    def speed_up(self) -> None:
        if self.speed == 3:
            print("At max speed")
        else:
            self.speed += 1
            print("Fan speed increased")

    def speed_down(self) -> None:
        if self.speed == 0:
            print("Fan is off")
        else:
            self.speed -= 1 
            print("Fan speed decreased")

    def status(self) -> None:
        if self.speed == 0:
            print("Fan is turned off")
        elif self.speed == 1:
            print("Fan is at lowest setting")
        elif self.speed == 2:
            print("Fan is at medium setting")
        else:
            print("Fan is at highest setting")




class WaterBottle:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.amount = 0 

    def fill(self, ml: int) -> None:
        space = self.capacity - self.amount
        if ml > space:
            self.amount = self.capacity
            overflow = ml - space
            print(f"Bottle filled. {overflow}ml overflowed..")
        else:
            self.amount = self.capacity

    def drink(self, ml: int) -> None:
        if ml > self.amount:
            available = self.amount
            self.amount = 0
            print(f"You only have {available}ml")
        else:
            self.amount -= ml
            print(f"You drank {ml}ml water")

    def percent_full(self) -> float:
        return (self.amount / self.capacity) * 100
        


       
            
class Item:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name 
        self.weight = weight 
    def display_info(self, index: int) -> None:
        print(f"{index}: {self.name} - {self.weight}g")


class Backpack:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.items = []

    def total_weight(self) -> int:
        total = 0
        for item in self.items:
            return total

    def add_item(self, item: str) -> None:
        
        