def main():
    count = 0
    grades = 0
    while True:
        new_grade = float(input("Enter a grade (type -1.0 to stop): "))
        if new_grade == -1.0 and count == 0:
            print("You entered zero grades")
            break
        elif new_grade == -1.0 and count != 0:
            average = grades / count
            print(f"you entered {count} grades, the average {average:.2f}")
            break
        else:
            grades += new_grade
            count += 1
main()
