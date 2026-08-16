def main():
    num_list = [5, 9, 10, 25, 37, 40]
    new_list = []
    for item in num_list:
        if item % 5 == 0:
            new_list.append(item)
    print(new_list)
if __name__ == "__main__":
    main()

