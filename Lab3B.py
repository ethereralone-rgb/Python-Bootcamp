"""GPA Calculator
o	Write a program that reads from the user the number of hours and quality points earned for four courses.
o	Make sure to read these inputs as integers.
o	Then calculates the Total Hours, Total Quality Points, and the GPA.
o	Finally, output the Total Hours, the Total Quality Points, and the GPA.
o	When printing the total amount of hours and quality points, print them as integers.
o	When printing the GPA, print it as a float, rounded to 2 decimal places.
"""
if __name__ == "__main__":
            courses = []
            grades = []

            for i in range(4):
                    course = int(input(f"Course {i+1} Hours: "))
                    grade = int(input(f"Grade for course {i+1}: "))
                    courses.append(course)
                    grades.append(grade)
            total_hours = courses
            GPA = (courses * grades/ courses)
            TQP = grades
            print(f"Total hours: {total_hours}")
            print(f"Total quality points: {TQP}")
            print(f"Your GPS for thsi semester is {GPA}")