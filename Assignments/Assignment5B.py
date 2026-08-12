import random

def print_chart(grid):
    for row in grid:
        print(" ".join(row))
    

def main():
    
    rows = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    
    grid = []
    available_seats = 0 
    for r in range(rows):
        row = []
        for c in range(col):
            chance = random.random()
            if chance >= 0.7:
                row.append("R")
            else:
                row.append("A")
                available_seats += 1 
        grid.append(row)
    print_chart(grid)
    print(f"Number of available seats: {available_seats}")
    print()
   
    while available_seats > 0:
        chosen_row = int(input(f"Enter the row number (0 to {rows - 1}): "))
        chosen_cols = int(input(f"Enter the column number (0 to {col - 1}): "))
        seat = (chosen_row, chosen_cols)

        if grid[chosen_row][chosen_cols] == "A":
            grid[chosen_row][chosen_cols] = "B"
            available_seats -= 1
            print("Seat booked succesfully!")
        elif grid[chosen_row][chosen_cols] == "R":
            print("This seat is already reserved")
        elif grid[chosen_row][chosen_cols] == "B":
            print("This seat has already been booked.")
        print_chart(grid)
        print()

        
            



if __name__ == "__main__":
    main()