def last_and_first(string):

    last = string[-1]
    first = string[0]
    if first == last:
        return True
    else:
        return False

def main():
    listy = [10, 3, 4, 9, 10]

    print(f"Given List: {listy} Result: {last_and_first(listy)}")


    
if __name__ == "__main__":
    main()