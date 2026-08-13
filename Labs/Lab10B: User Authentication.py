""" Build a program that authenticates the user login by asking the user for a username and a password. 
For this program, you are going to use a dictionary to store the users data. 
This is not ideal but just for this lab 
we are going to use the users username as the key and the password as the value for the username key.
"""


def main():
    # Create dictionary to hold username/password 
    password_storage = {}
    log_in = False
    # Create a menu that loops 
    while True:

        # Present option then ask for user input 
        print("Choose an option")
        print("1 - Login \n2 - Register \n3 - Exit")
        option = int(input(" "))

        # if user chooses option one they are logging in. 
        if option == 1:
            print("[Login]")
            username = input("Username: ")
            password = input("Password: ")

            # Check to see if the username has the corresponding password 
            if password_storage.get(username) == password:
                print("Success!")
                log_in = True
            else:
                print("Incorrect username/password!")

        # Register a username with password 

        elif option == 2:
            print("[Register]")
            username = input("Username: ")
            password = input("Password: ")

            # Check if username is in the dictionary
            if username in password_storage:
                print("Username already Taken!")
            else:
                # Create an account
                password_storage[username] = password
                print("Account Created")

        elif option == 3:
            # log out if you are not logged in
            if log_in == False:
                print("Goodbye!")
                break
            else:
                # Logout message if you are logged in 
                print("Logging out!.... Goodbye!")
                break

if __name__ == "__main__":
    main()
                            
        