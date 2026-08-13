def menu():
    print()
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")
    print("Make your selection: ")

def main():
    mailing_list = []


    while True:
        menu()
        try:
            option = int(input("Make your selection: "))
        except ValueError:
            print()
            print("Error. Please make a selection (1-4).")
            print()
            continue
        
        print() 

        if option == 1:
            email = input("Enter the email: ")
            mailing_list.append(email)
            print("Email added to mailing list.")
            print()

        elif option == 2:
            delete_email = input("Enter the email to be removed: ")
            if delete_email in mailing_list:
                mailing_list.remove(delete_email)
                print("Email removed from mailing list.")
            else:
                print("No such email in mailing list.")

        elif option == 3:
            print(mailing_list)

        elif option == 4:
            print("Shutting down...")
            break
        else:
            print("Error. Please make a selection (1-4)")


if __name__ == "__main__":
    main()