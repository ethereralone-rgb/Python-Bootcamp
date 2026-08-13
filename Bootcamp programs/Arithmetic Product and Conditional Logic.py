def product(x,y):
    product = x * y 
    if product <= 1000:
        return product
    else:
        sum = x + y
        return sum


def main():
    x = int(input("Number1: "))
    y = int(input("Number2: "))
    print(product(x,y))

if __name__ == "__main__":
    main()
