"""Julian Hamlet 
o	Prompt the user to enter a total number of minutes
o	Read the input as a float
o	Convert the total minutes into:
▪	Total days
▪	Remaining hours
▪	Remaining minutes
o	Round the remaining minutes to 2 decimal places.
"""



if __name__ == "__main__":
    print("[Time Cnoverstion - Minutes to Days, Hours, and Minutes]")

    user_minutes = float(input("Enter the total minutes: "))

    days = int(user_minutes // 1440)
    leftover_days = (user_minutes % 1440)
    hours = int(leftover_days // 60)
    minutes = (leftover_days % 60)

    print(f"{user_minutes} minutes is approximately {days} day(s), {hours} hours, and {minutes:.2f} minutes.")