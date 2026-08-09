
def isValid(height, width):
    if height + width > 30:
        return True
    else:
        return False 

def area(height, width):
    area = height * width
    return area 

def perimeter(height, width):
    perimeter = (height * 2) + (width *2)
    return perimeter







def main():
    while True:
        width = float(input("Enter a width: "))
        height = float(input("Enter a height: "))
        isValid(height, width)

        if isValid(height, width):
            print("This is a valid Triangle")
            True_area = area(height, width)
            True_P = perimeter(height, width)
            print(f"The area is: {True_area}")
            print(f"The perimeter is: {True_P}")
            print()
            option = input("Do you want to enter another width and height (Y/N)?: ").upper()

            if option != "Y":
              break
            
        else:
            print("This is an invalid Triangle")
            print("Do you want to enter another triangle (Y/N): ")
            option = input("> ").upper()

            if option != "Y":
                break










if __name__ == "__main__":
    main()