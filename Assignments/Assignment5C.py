""" Matrix Multiplication. Write a Python program that takes input for two matrices, 
validates whether matrix multiplication is possible, 
and if valid, displays both input matrices and their resulting product matrix.
All matrix values must be entered by the user 
as comma-separated values on a single line. 
The program must internally divide these values into rows 
and columns based on the dimensions entered by the user
"""

# function to display the matrix 
def print_matrix(grid):
    # go through each row in the matrix 
    for row in grid:
        # go through each value in the matrix 
        for value in row:
            print(value, end= " ")
        # move to the next line after finishing a row 
        print()



def main():
    
    # Get the dimensions of  matrix A
    rows1 = int(input("Enter rows for Matrix A: "))
    cols1 = int(input("Enter the columns for Matrix A: "))

    print()
    # Get the dimensions of Matrix B
    rows2 = int(input("Enter rows for Matrix B: "))
    cols2 = int(input("Enter the columns for Matrix B: "))

    # Matrix multiplication only possible when 
    # the number of columns in A equals the number of rows in B. 
    if cols1 != rows2:
        print("Martix multiplication is not possible! Goodbye!")

    else:
        # --------------
        # Build Matrix A
        # --------------

        # Get all Matrix A values on one line.
        matrixA_input = input("Enter the Matrix A values (comma-seperated):  ")

        # Split the input string into a list 
        matrixA_values = matrixA_input.split(",")

        # Create empty list that will old all rows of Matrix A
        matrixA = [] 

        # Keeps track of what value we will be using
        matrixA_count = 0  

        # Create each row of Matrix A
        for r in range(rows1):
            row =[]

            # Add the correct number of values to the current row 
            for c in range(cols1):
                row.append(int(matrixA_values[matrixA_count]))
                matrixA_count += 1

            # Add the completed row to Matrix A
            matrixA.append(row)

        # --------------
        # Build Matrix B
        # --------------

        # Get all of Matrix B values 
        matrixB_input = input("Enter the Matrix B values (comma-seperated):  ")

        # Split the input string into a list 
        matrixB_values = matrixB_input.split(",")

        # Empty list that will hold all rows of Matrix B
        matrixB = []

        # Keeps track of what value we are currently using
        matrixB_count = 0 

        # Create each row of Matrix B
        for r in range(rows2):
            row = []

            # Add the correct number of values to the current row 
            for c in range(cols2):
                row.append(int(matrixB_values[matrixB_count]))
                matrixB_count += 1

            # Add the completed row to Matrix B 
            matrixB.append(row)

        # ------------------------
        # Display the Two Matrices
        # ------------------------
        print()
        print("Matrix A:")
        print_matrix(matrixA)

        print()
        print("Matrix B:")
        print_matrix(matrixB)

    # --------------------------
    # Build the Matrices product
    # --------------------------

    matrix_product = []

    for r in range(rows1):
        product_row = []

        for c in range(cols2):
            total = 0

            for k in range(cols1):
                total += matrixA[r][k] * matrixB[k][c]

            product_row.append(total)

        matrix_product.append(product_row)

    # Display the product 

    print()
    print("Matrix Product:")
    print_matrix(matrix_product)




if __name__ == "__main__":
    main()