
def numerals(s):
    values = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, 
                "C" : 100, "D" : 500, "M" : 1000}
    totalNumber = 0
    for i in range(len(s)- 1):
        if values[s[i]] >= values[s[i + 1]]:
            totalNumber += values[s[i]]
        else:
            totalNumber -= values[s[i]]
    totalNumber += values[s[len(s) -1]]                              
    return totalNumber


def main():
    s = input("Enter roman numerals: ")
    s = numerals(s)
    print(s)


if __name__=="__main__":
    main()
