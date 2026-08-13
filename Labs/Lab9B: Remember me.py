def menu():
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")

def main():
    friend_list = []
    while True:

        print("[Friend List]")
        menu()
        print()

        try:
            option = int(input("Make your selection: "))
        except ValueError:
            print()
            print("Error. Please make a selection 1-3.")
            print()
            continue

        print()

        if option == 1:

            name = input("Enter your friends name: ")
            age = int(input("Enter your friends age: "))
            friend_list.append((name,age))

            print("Friend Added.")

        elif option == 2:

            if not friend_list:
                print("Friend List empty.")

            for name, age in friend_list:
                print(f"Name: {name} , Age: {age}")
                

        elif option == 3:
            print("Shutting down...")
            break



    pass
if __name__ =="__main__":
    main()