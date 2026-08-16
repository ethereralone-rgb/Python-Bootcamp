"""
Creating a program that counts the vowels in a from a given input
"""


def main():
    vowels = ["a", "e", "i", "o", "u"]
    count = 0 
    string = input("Enter a sentence: ").lower()

    for char in string:
        if char in vowels:
            count += 1
    print(f"Number of vowels: {count}")



if __name__ =="__main__":
    main()