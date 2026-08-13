def allmath(x,y):
     results = ()
     results = results + (x + y,)
     results = results + (x - y,)
     results = results + (x * y,)

     if y == 0:
          results = results + (None, None, None)
     else: 
          results = results + (x / y,)
          results = results + (x // y,)
          results = results + (x % y,)
     results = results + (x ** y,)
     return results


def main():
     x = int(input("Enter the first number: "))
     y = int(input("Enter the second number: ")) 
     print(allmath(x,y))

if __name__ == "__main__":
     main()


     