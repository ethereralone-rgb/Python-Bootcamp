"""o	The program will prompt the user to enter how many of each sandwich type needs to be cooked. 
o	Make sure to read these inputs as integers.
o	It will then print out the number of sandwiches entered for each sandwich type on separate lines. 
o	Calculate the total amount of time the oven will have to run to cook them all. 
o	Output the cooking times in minutes and seconds.
"""




if __name__ == "__main__":
               
    small_sandwhich = int(input("Enter the number of small sandwhiches: "))
    total_small = (small_sandwhich * 30)

    medium_sandwhich = int(input("Enter the number of medium sandwhiches: "))
    total_medium = (medium_sandwhich * 60)

    large_sandwhich = int(input("Enter the number of large sandwhiches: "))
    total_large = (large_sandwhich * 75)


    xlarge_sandwhich = int(input("Enter the number of extra-large sandwhiches: "))
    total_xl = (xlarge_sandwhich * 135)

    total_seconds_cook = total_small + total_medium + total_large + total_xl
    total_minutes_cook = total_seconds_cook // 60
    remaining_seconds = total_seconds_cook % 60

    print(f"You've entered {small_sandwhich} small sandwhiches.")
    print(f"You've entered {medium_sandwhich } medium sandwhiches.")
    print(f"You've entered {large_sandwhich} large sandwhiches.")
    print(f"You've entered {xlarge_sandwhich} extra-large sandwhiches.")
    print(f"Total cooking time is {total_minutes_cook} minutes and {remaining_seconds} seconds")