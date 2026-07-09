""" This program will calculate a car's total stopping distance on a road. the total
stopping distance is calculated as the sum of the reaction distance and braking distance
The formula for stopping distance  d= (1.47 x v x t) + v squared // 30 x f """


if __name__ == "__main__":
    REACTION_CONST = 1.47
    BRAKE_CONST = 30
    FRICTION_MULTIPLIER = 0.85

    print("[Highway Stopping Distance Calculator]")
    speed = float(input("Enter the speed(in mph): "))  # User enters speed
    reaction_time = float(input("Enter the reaction time (in seconds): "))  # User enters reaction time
    road_friction = float(input("Enter the road friction coefficient (mu): "))  # User enters road friction

    F =  road_friction * FRICTION_MULTIPLIER # calculate friction factor
    distance1 = (REACTION_CONST * speed * reaction_time) # calculate first half of
    distance2 = (speed * speed) / (BRAKE_CONST * F)
    Distance3 = distance1 + distance2
    print(f"The estimated stopping distance is {Distance3:.2f} feet.")

