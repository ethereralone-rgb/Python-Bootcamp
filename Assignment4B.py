""" Write a Python program that checks whether a password meets security requirements. The program should continuously prompt the user until they enter a strong password."""

def check_length(password):
    return len(password) >= 8

    
def check_upper_lower(password):
    is_upper = False
    is_lower = False
    for char in password:
        if char.isupper(): 
            is_upper = True
        if char.islower():
            is_lower = True
    return is_upper and is_lower

def check_special_character(password):
    special_char = False
    for char in password:
        if char in ("!","@","#"):
            special_char = True
    return special_char

def main():
    while True:
        print_phrase = "Password does not meet the requirements: "
        password = input("Enter a password: ")

        if not check_length(password):
            print_phrase += " Must be at least 8 characters long."

        if not check_upper_lower(password):
            print_phrase += " Must contain both uppercase and lowercase letters."

        if not check_special_character(password):
            print_phrase += " Must include at least one special character (!, @, #)."

        if print_phrase == "Password does not meet the requirements: ":
            print("Password is Strong!")
            break
        else: 
            print(print_phrase)
        

if __name__ == "__main__":
    main()





    
        

    
            

