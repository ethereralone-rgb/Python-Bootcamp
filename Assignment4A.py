"""Write a Python program that converts a given text into Pascal Case by implementing two functions:
format_word(word) – This function should take a single word as input, capitalize its first letter, and convert the rest of the letters to lowercase.Finally this function will return the converted/formatted word.
convert_to_pascal_case(text) – This function should iterate through the entire string. When it encounters a space character, it should treat the collected word as complete and call another function to convert that word to Pascal Case. Once the full string is processed, it should return the final Pascal Case string.
"""

def convert_to_pascal_case(word):
    x = " "
    y = " "
    for char in (word):
        if char != " ":
            y += char
        else:
            x += char
    return x



def convert_to_pascal_case():


def main():
