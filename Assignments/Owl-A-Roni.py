class Recipe:
    def __init__(self,cheese:str, serving: int= 1)-> None:
        self.cheese = cheese
        self.serving = serving
    def new_amount(self, amount):
        return amount * self.serving


        
def main():

    serving = int(input("How many servings of Owl-A-Ronis?: "))
    cheese = input("What type of cheese?: ")
    print()
    print("Generating recipe...")
    print()
    print("Recipe:")
    print("1. In a pot add:")
    print(f"     - {serving * 0.5} cup of Owl-A-Ronis")
    print(f"     - {serving * 0.5} cup of water")
    print(f"     - {serving * 1} pinch of salt")
    print("2. Boil the pasta in water for about 6 to 8 minutes")
    print("3. Drain excess water")
    print(f"4. Shred {serving * .25} cup of {cheese} cheese")
    print(f"5. Pour {serving * 1} splash of Milk into the pot")
    print(f"6. Add the shredded {cheese} cheese into the pot")
    print("7. Stir well until creamy")

    


if __name__ == "__main__":
    main()