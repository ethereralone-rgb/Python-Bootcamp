import random


def main():
    
    rows = int(input("Enter the rows: "))
    col = int(input("Enter the col: "))
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
    for row in grid:
        print(row)
    print(available_seats)

if __name__ == "__main__":
    main()