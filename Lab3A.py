""" Credit card APR program. this program will calculate the users input and give them the monthly percentage rate and the minimum payment needed
I will write that prompts a user for their current balance on their credit card and their annual percentage. ALL INPUTS need to be read as FLOATS
Program should calculate the Monthly Percentage Rate by dividing the APR by 12
Use the Monthly Percentage Rate(MPR) to calculate the Minimum Payment. Remember to use the MPR as a decimal value for this calculation by dividing it by 100
You can calculate this value by multiplying the current balance on the credit card (Amount Owed) times the Monthly Percentage Rate:
Amount owed X Monthly Percentage Rate = Minimum Payment
or Amount Owed X APR / 12 = Minimum Payment"""

if __name__ == "__main__":
            Amount_owed = float(input("Amount Owed: "))  # ask use for Amount Owed
            APR = float(input("APR: "))   # Ask user for APR

            MPR = float(APR / 12)  # calculation for MPR
            Minimum_payment  = (Amount_owed * MPR/ 100)  # calculation for Minimum payment

            print(f"Monthly Percentage Rate: {MPR:.2f}")
            print(f"Minimum payment: ${Minimum_payment:.2f}")



