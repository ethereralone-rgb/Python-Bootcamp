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
            total += item.weight
        return total

    def add_item(self, item: Item) -> None:
        if self.total_weight() + item.weight > self.max_weight:
            print(f"Cannot add {item.name}. Backpack would be over its {self.max_weight}g")
        else:
            self.items.append(item)
            print(f"Successfully added {item.name}")

    def show_all(self) -> None:
        if len(self.items) == 0:
            print("Backpack is empty.")
            return
        print("Items in backpack")
        for i in range(len(self.items)):
            self.items[i].display_info(i)


class BankAccount:
    # __init__ runs automatically when you write "BankAccount("Ada", 100)"
    # The double underscores mark it as a "dunder" method (double-underscore) method,
    # meaning Python calls it for you rather than you calling it by name
    # owner: str balance: int are hints describing what to pass in
    # -> None: because __init__ sets things up, it doesnt hand the value back 
    def __init__(self, owner: str, balance: int) -> None:
        # self.owner stores the name ON the object, so every method can reach it 
        # The bare "owner" on the right is hte parameter that was passed in.
        self.owner = owner
        self.balance = balance 
        # empty list that grows as the bank account does
        self.history = []

    def deposit(self, amount: int) -> None:
        # a guard clause that catches the bad case first and leaves immediatly. 
        # <= covers both zero and a negative in one check
        if amount <= 0:
            print("The deposit must have a positive amount.")
            # return here so the code never runs if this isnt valid
            return

        # passes the guard. amount gets added to balance
        self.balance += amount

        # .append add one element to the end of the list
        # An f-string builds the log entry, so the list holds things like "Deposit: 50"
        self.history.append(f"Deposit: {amount}")
        print(f"Deposited {amount}. New balance {self.balance}")

    def withdraw(self, amount: int) -> None:
        # guard 1: check to make sure its a positive number 
        if amount <= 0:
            print("Withdraw must be positive amount")
            return
        # Guard 2: Overdraft. checked before touching self.balance,
        # because theres no way to undo a subtraction you shouldnt have made
        
        if amount > self.balance:
            print(f"Insufficient funds balance is {self.balance} ")
            return

        # both guard passed 
        self.balance -= amount
        self.history.append(f"Withdrawl {amount}")
        print(f"Withdrew {amount}. New balance: {self.balance}")


    # __str__ is a dunder like __init__ , and like __init__ you never call it directly 
    # Python calls it for you whenever the object needs to become 
    # text: print(acct), str(acct), or an f-string containing {acct}
    # -> str because it RETURNS a string. it does not print 

    def __str__(self):
        return f"{self.owner}'s account: Balance: {self.balance}"

    def print_history(self) -> None:
        # Empty list guard that checks to make sure the length is correct
        if len(self.history) == 0:
            print("No transactions yet.")
            return
        print(f"Transaction history for {self.owner}")

        # enumerate hands back position and value together each pass
        # start=1 makes it count 1,2,3 instead of 0,1,2
        # This is a cleaner alternative to the 
        # range(len(..)) 
        for i, entry in enumerate(self.history, start=1):
            print(f"{i}. {entry}")


class Room:
    # name: what to call the room, current_temp: how warm it is right now
    def __init__(self, name: str, current_temp: int) -> None:
        self.name = name 
        self.current_temp = current_temp


    # -> str not None becuase this will returns text instead of printing it 
    # caller decides what to do with it 
    def __str__(self) -> str:
        return f"{self.name} is {self.current_temp} degrees"

class Thermostat:
    def __init__(self, target_temp: int) -> None:
        self.target_temp = target_temp

    # Room is a hint. Like saying "Pass me a Room object"
    def regulate(self, room: Room) -> None:
        # room.current_temp reaches into the OTHER object to read its data.
        # self.target_temp reads this thermostat's own data 
        # Both dots mean the same thing "Look into this object"
        if room.current_temp < self.target_temp:
            room.current_temp += 1 
            print(f"Heating {room.name}.... now {room.current_temp}")

        elif room.current_temp > self.target_temp:
            room.current_temp -= 1
            print(f"Cooling {room.name}... now {room.current_temp}")


        else:
            # neither less nor greater so they are equal, no change needed
            print(f"{room.name} is at target({self.target_temp})")
