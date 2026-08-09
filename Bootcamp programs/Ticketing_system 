""" “Owl World” a KSU-themed theme park,  is about to open. But they are missing their ticketing system which you are in charge in developing.

Owl World charges $28.00 to adults and $24.00 to children for a 1-day entry ticket. While for customers with an account they get a $6.00 discount per ticket, charging $22.00 to adults and $18.00 to children.

With your program, the user should be able to buy tickets but also be able to register and sign in to be able to get the discount. """

# Program written by Julian Hamlet 


def buy_tickets(signed_in):
    if signed_in == True:
        Adult = 22.00
        Children = 18.00
    else:
        Adult = 28.00
        Children = 24.00

    print(f"Ticket Prices: \n Adult: ${Adult}, Children: ${Children}")
    option_one = int(input("How many Adult tickets?: "))
    option_two = int(input("How many Children tickets?: "))

    total_Adult = option_one * Adult 
    total_Children = option_two * Children
    total = total_Adult + total_Children

    print(f"Processing...\n {option_one}x Adult Tickets ---- ${total_Adult}\n {option_two}x Children Tickets ---${total_Children}\n Total: ${total}" )
    return total

def my_Account(name, saved_password, signed_in):

    print("Choose an option:\n 1.Sign-in\n2.Register")
    option = input(">")

    if option == "2":

        username = input("Username: ")
        name = username
        password = input("Password: ")
        saved_password = password

        print("Registration Successful!")
        return name, saved_password, signed_in
    
    elif option == "1":
        username = input("Username: ")
        password = input("Password: ")
        if username != name or password != saved_password:
            print("Incorrect Username/Password")
        else:
            signed_in = True
            print("Login Successful")
    return name, saved_password, signed_in
        




def main():
    name = ""
    saved_password = ""
    print('[Owl World]')
    signed_in = False

    while True:
        if signed_in == True:
            print(f"Welcome {name}!")
        
        print("Choose an option: \n '1. Buy Tickets'\n '2. My account'\n '3. Exit'")
        option = input("> ")

        if option == "1":
            buy_tickets(signed_in)

        elif option == "2":
            name, saved_password, signed_in = my_Account(name, saved_password, signed_in)

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Error please enter an option 1-3")

        

if __name__ == "__main__":
    main()
