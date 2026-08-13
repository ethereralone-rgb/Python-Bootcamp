import random
def print_chart(grid):
    for row in grid:
        print(" ".join(row))
    
def main():
    rows = int(input("Enter a number of rows: "))
    cols = int(input("Enter a nubmer of columns: "))
    

    mine_field = []
    uncovered_mines = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            chance = random.random()
            if chance < 0.25:
                row.append("M")
                uncovered_mines += 1
            else:
                row.append(".")
        mine_field.append(row)
    print_chart(mine_field)
    print(f"Number of mines: {uncovered_mines}")
    print()
    while uncovered_mines > 0:
        chosen_row = int(input(f"Enter the row (0 - {rows - 1}): "))
        chosen_col = int(input(f"Enter the column (0 - {cols - 1}): "))
        if mine_field[chosen_row][chosen_col] == "M":
            uncovered_mines -= 1 
            mine_field[chosen_row][chosen_col] = "X"
            print("You found a mine!... mine disamred!")
            print_chart(mine_field)
        elif mine_field[chosen_row][chosen_col] == "X":
            print("You already found this mine!")
            print_chart(mine_field)
        else:
            print("There is no mine here!")
        if uncovered_mines == 0:
            print("All mines have been found")
            break
    print_chart(mine_field)

if __name__ == "__main__":
    main()