"""
Write a program to check if a given number is a palindrome
"""

def main():
    numbs = 121
    pal_numbs = str(numbs)
    new_number = pal_numbs[::-1]

    if pal_numbs == new_number:
        print("This number is a plaindrome")
    else:
        print("this number is not a plaindrome")



if __name__ == "__main__":
    main()

def get_odd(numbers):
    return [n for n in numbers if n % 2 != 0]

def get_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def sort_list(x, y):
    return sorted(x + y)
    
def main():
    first = [10, 20, 25, 30, 35]
    second = [40, 45, 60, 75, 90]
    print(sort_list(get_odd(first), get_even(second)))
    
    
if __name__ == "__main__":
    main()

def main():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i*j, end="\t")
        print("\n")
if __name__ == "_main__":
    main()