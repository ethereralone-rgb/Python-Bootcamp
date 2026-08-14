

def main():
    
    running_sum = 0
    previous_num = 0
    # iterate over each number in the range of numbs (1-9)
    for i in range(10):
        running_sum = i + previous_num
        print(f"Current number {i} Previous number {previous_num} Sum {running_sum}")
        # replace number with old i 
        previous_num = i
if __name__ == "__main__":
    main()