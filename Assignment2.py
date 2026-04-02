#Assignment_2 by Mark fileivich (2582700)
#Question 1 Removing duplicates and sorting
def main():
 num_readings = int(input("Enter how many readings (number) will you enter:"))
 inputed_readings = []
 for i in range(num_readings):
     list_1 = float(input(f"Enter reading {i+1}:"))
     inputed_readings.append(list_1)
 if len(inputed_readings) > 0:
     sorted_numbers = sorted(inputed_readings)
     No_duplicates= set(sorted_numbers)
     print ("full list:",inputed_readings)
     print ("sorted list with no duplicates:",No_duplicates)
 else:
   print("No readings so empty list")
 #Question 2 cumulative sum
 num_readings_2 = int(input("Enter how many readings (number) will you enter:"))
 inputed_readings_2 = []
 total = 0
 for i in range(num_readings_2):
     list_2 = float(input(f"Enter reading {i+1}:"))
     total += list_2
     inputed_readings_2.append(total)
 if len(inputed_readings_2) > 0:
    print("The cumulative sum of the previous element list is:",inputed_readings_2)
 else:
    print("No readings so empty list")
 #Question 3 slicing
 num_readings_3 = int(input("Enter how many readings (number) will you enter:"))
 inputed_readings_3 = []
 for i in range(num_readings_3):
     value = float(input(f"Enter reading {i+1}:"))
     inputed_readings_3.append(value)
 step_value = int(input("Enter the step value:"))


 if step_value <= 0:
    answer = 0
    print(num_readings_3)
 else:
    answer = 0
    answer = inputed_readings_3[step_value-1::step_value]
 print(answer)
 #Question 4 Dot product
 num_readings_4 = int(input("Enter how many readings (number) will you enter for the first list:"))
 inputed_readings_4 = []
 for i in range(num_readings_4):
     value = float(input(f"Enter reading {i+1}:"))
     inputed_readings_4.append(value)
 num_readings_5 = int(input("Enter how many readings (number) will you enter for the second list:"))
 inputed_readings_5 = []
 for i in range(num_readings_5):
     value = float(input(f"Enter reading {i+1}:"))
     inputed_readings_5.append(value)
 if len(inputed_readings_4) != len(inputed_readings_5):
     print("Error, The two lists must have the same number of readings.")
 else:
     dot_product = sum(a * b for a, b in zip(inputed_readings_4, inputed_readings_5))
     print("The dot product of the two lists is:", dot_product)
 # Question 5 Matrix Multiplication
 num_rows_1 = int(input("Enter the number of rows for the first matrix:"))
 num_cols_1 = int(input("Enter the number of columns for the first matrix:"))
 matrix_1 = []
 for i in range(num_rows_1):
     row = []
     for j in range(num_cols_1):
         value = float(input(f"Enter value for matrix 1 at position ({i+1}, {j+1}):"))
         row.append(value)
     matrix_1.append(row)
 num_rows_2 = int(input("Enter the number of rows for the second matrix:"))
 num_cols_2 = int(input("Enter the number of columns for the second matrix:"))
 if num_cols_1 != num_rows_2:
     print("Error, The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
 else:
     matrix_2 = []
     for i in range(num_rows_2):
         row = []
         for j in range(num_cols_2):
             value = float(input(f"Enter value for matrix 2 at position ({i+1}, {j+1}):"))
             row.append(value)
         matrix_2.append(row)
     result_matrix = []
     result_matrix = [[0 for _ in range(num_cols_2)] for _ in range(num_rows_1)]
     for i in range(num_rows_1):
         for j in range(num_cols_2):
             for k in range(num_cols_1):
                 result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
     print("The result of matrix multiplication is:")
     for row in result_matrix:
         print(row)
if __name__ == "__main__":
    main()