def menu():
    print("--- OWL DINER ---")
    print("Owl Burger   $3.50")
    print("Talon Fries. $2.50")
    print("Hoot Soda.   $1.50")



def main():
        burger_price = 3.50
        fries_price = 2.50
        soda_price = 1.50
        menu()
        print()
        burgers_amount = int(input("How many Owl burgers?: "))
        fries_amount = int(input("How many Talon Fries?: "))
        sodas_amount = int(input("How many Hoot Sodas?: "))

        total_burgers = burger_price * burgers_amount
        total_fries = fries_price * fries_amount
        total_soda = soda_price * sodas_amount
        total_soda = int(total_soda)
        sub_total = float(total_burgers + total_fries + total_soda)
        tax = (sub_total * 7) / 100
        total = sub_total + tax

        print("--- OWL DINER ---")
        print(f"Owl Burger    x{burgers_amount}    {total_burgers:.2f}")
        print(f"Talon Fries   x{fries_amount}    {total_fries:.2f}")
        print(f"Hoot Soda     x{sodas_amount}    {total_soda:.2f}")
        print(f"Subtotal:             {sub_total:.2f}")
        print(f"Tax (7%):             {tax:.2f}")
        print(f"Total:                {total:.2f}")

if __name__ == "__main__":
      main()