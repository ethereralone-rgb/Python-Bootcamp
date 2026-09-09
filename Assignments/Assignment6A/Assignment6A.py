"""
Creating a To-Do list program. Need to define a class for my To-Do items.
Because I will be handling multiple To-Do items, such as buying groceries or 
going to class. I will need to create a list for these items to go inside. 
"""


# sets up class Todo with a title, date, time and if the item is done. set the "done" attribute to false because all 
# items are not done initally

class Todo:    # initalize the to-do class
    def __init__(self, name: str, date: str = None, time: str = None)-> None:
        self.name = name
        self.date = date
        self.time = time 
        self.done = False

    # Returns the value of the item in the to-do list
    def has_due_dt(self)-> bool: 
        return self.date is not None and self.time is not None
            

    # sets the item on to-do list as done or not done represented by Boolean Values 
    def set_done(self)-> None:
        if self.done != True:
            self.done = True
        
    # Shows the status of an item on the Todo list 
    def is_done(self):
        return self.done 

    # Changes item due date and time 
    def set_date_time(self, date: str, time: str)-> None:
        self.date = date 
        self.time = time 

    # Returns the value of the item in list 
    def get_todo(self)-> str:
       
        return (f"{self.name}\n\tDue: {self.date} at {self.time}")


# prints the To-do list 
def To_Do_list():
    print("[TO DO LIST]")
    print("1 - Add a To-do list item")
    print("2 - Set a To-do item as done")
    print("3 - Set or change the due date and time of a To-do item")
    print("4 - Remove a To-do list item due date and time")
    print("5 - Print To-do list")
    print("6 - Exit")

def main():
    pass
    todo_list = { 

    }
    while True: 
        To_Do_list()
        choice = int(input("Please choose an option 1-6: "))

        if choice not in range(1,7):
            print("Please choose an option 1-6").strip()

        if choice == 6:
            print("Goodbye")
            break

        elif choice == 1:
            has_time = input("Does your To-Do item have a due date and time? (y/n): ").lower().strip()
            if not has_time:
                break
            if has_time not in ("y", "n"):
                print("Please enter y or n.")
                continue 

            title = input("What is the title: ").strip()

            if has_time == "n": # if the item doesnt have a set time and date just get the name 
                todo_list[title] = { "Date": None, "Time": None}
        
            if title in todo_list: # if the item is in the list already 
                print("An item with this title already exists")
                continue
            if has_time == "y":
                due_date = input("Enter the due date (MM/DD/YYY): ").strip()
                due_time = input("Enter the due time (HH:MM AM/PM): ").strip()
                todo_list[has_time] = { "Date": due_date, "Time": due_time}
            else:
                todo_list[title] = Todo(title, due_date, due_time)

            print("Adding your To-do list item...")

        elif choice == 2:  # change the status of item and change it to done
            title = input("Please enter the name of your item: ")
            if title not in todo_list:
                print("No item with that title")
            else:
                todo_list[title].set_done()
                print(f"{title} is marked as done")

        elif choice == 3: # set or change the due date and time 
            print("Select an item to change on the ")

            for index, item in enumerate(todo_list): # list the items on the list with the index 
                print(index, item.name)

            selection = input("> ")
            due_date = input("Enter the due date (MM/DD/YYYY): ")
            due_time = input("Enter the due time (HH:MM AM/PM): ")
            todo_list[selection].set_date_time(due_date, due_time) # changes the due date and time of item

        elif choice == 4:
            for index, item in enumerate(todo_list):
                print(index, item.name)

            selection = input("> ")
            todo_list[selection].set_date_time(None, None)

        elif choice == 5:
            for item in todo_list:
                if not item.is_done():
                    print("-", item.get_todo())

                

if __name__ == "__main__":
    main()