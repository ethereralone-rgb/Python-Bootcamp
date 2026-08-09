def main():
    E_string = 82.41
    A_string = 110.00
    D_string = 146.83 
    G_string = 196.00
    B_string = 246.94
    e_string = 329.63 

    tune_counter = 0 
    print("Let's tune your guitar!")
    while True:
            if tune_counter == 0:
        
                string_name = "sixth"
                target = E_string
        
            elif tune_counter == 1:
        
                string_name = "fifth"
                target = A_string
        
            elif tune_counter == 2:
        
                string_name = "fourth"
                target = D_string
        
            elif tune_counter == 3:
        
                string_name = "third"
                target = G_string
        
            elif tune_counter == 4:
        
                string_name = "second"
                target = B_string 
        
            elif tune_counter == 5:
                string_name = "first"
                target = e_string 

            tune_one = float(input(f"What is the frequency of the {string_name} string?: "))
            if tune_one == target:
                print("Perfect! You are in tune, let's move on to the next string...")
                tune_counter = tune_counter+1 
            elif tune_one > target:
                print("Too High! Loosen the string.")
            else:
                print("Too Low! Tighten the string.")
            if tune_counter == 6:
                print("Your guitar is tuned and ready to use!")
                break
main()
