def main():
    word = "pynative"
    print("Original string is", word)

    # Using the Slicing Method 
    # Format: [start:stop:step]
    even_chars = word[0::2]
    print("Printing only even index chars")
    for char in even_chars:
        print(char)

if __name__ == "__main__":
    main()