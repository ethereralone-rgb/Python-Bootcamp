import random
def print_chart(grid):
    for row in grid:
        print(" ".join(row))

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    dock_space = []
    open_space = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            chance = random.random()
            if chance < .4:
                row.append("F")
            else:
                row.append("E")
                open_space += 1
        dock_space.append(row)
    truck_pallets = int(input("Enter the number of pallets on truck: "))
    if truck_pallets > open_space:
        print("Cannot unload truck. Please leave.")
        return
    else:
        print(f"Number of open spaces: {open_space}")
    print()

    while truck_pallets > 0:
        print_chart(dock_space)
        unload_truck = int(input(f"Enter the row you want to unload at (0-{rows - 1}): "))
        unload_truck2 = int(input(f"Enter the column you want to unload at (0-{cols - 1}): "))
        if dock_space[unload_truck][unload_truck2] == "F":
            print("Cannot unload here pick another space.")
        elif dock_space[unload_truck][unload_truck2] == "E":
            open_space -= 1
            truck_pallets -= 1
            dock_space[unload_truck][unload_truck2] = "P"
            print("You filled this space, return for another pallet.")
            print(f"Remaining spaces: {open_space}")
            print(f"Remaining Pallets: {truck_pallets}")
        
        print("You already filled this space, pick another spot.")
    print_chart(dock_space)
    
            

            
                                 


    

    
               
            

        

if __name__ == "__main__":
    main()