"""
Create a list with 5 fruits. Add a new fruit at the end of the list 
then remove the one at (1) index
"""


def main():
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    fruits.append("fig")
    print(fruits)
    fruits.pop(1)
    print(fruits)

if __name__ == "__main__":
    main()


def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

def main():
    string = "Hello i am happy"

    reversed_String = reverse_string(string)

    print(reversed_String)
if __name__ == "__main__":
    main()

