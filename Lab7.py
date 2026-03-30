#Lab 7
#part 1
# My ID (2582700)
#d1 = 0
#d2 = 0
#k = (0 + 0) % 4 + 2 = 2
#shift = 0 - 0 = 0
#rows_keep = (0 % 2) + 2 = 2
def main():
 matrix = [[5,10,15,20,25],
              [30,35,40,45,50]
    ]
 Matrix_rectangle= list(matrix)
 print ("The original matrix")
 for row in Matrix_rectangle:
    print (row)
 print("Dimensions:")
 print("Rows =", len(Matrix_rectangle))
 print("Columns =", len(Matrix_rectangle[0]))
 last_column = [row[-1] for row in Matrix_rectangle]
 print("Last column:", last_column)
 
 first_3_cols = [row[:3] for row in Matrix_rectangle]
 print("All rows with only the first 3 columns:")
 for row in first_3_cols:
     print(row)
 #part B
 #Number of rows from our matrix = 2
 # with my ID 2582700
 Number_of_rows = len(Matrix_rectangle)
 d1 = 0
 d2 = 0
 k =  2
 shift =  0
 rows_keep = 2
 row_number = d1 % Number_of_rows
 chosen_row = d1 % len(matrix)
 old_row = Matrix_rectangle[chosen_row][:]
 new_row = [value + k for value in old_row]
 Matrix_rectangle[chosen_row] = new_row
 print("The new row added by k from the chosen row", chosen_row,"is", new_row)
 Starting_column = d2 % 2
 sub_array_sliced= [row[Starting_column:] for row in Matrix_rectangle]
 print(sub_array_sliced)
 print("\nChosen row index:", chosen_row)
 print("Old row:", old_row,"New row:", new_row)

 print("Matrix after row replacement:",Matrix_rectangle)

 print("Sliced sub-array from starting column", Starting_column)
 for row in sub_array_sliced:
        print(row)
 # since my last number in my ID is zero, This makes my chosen row be 0 and my k be 2 meaning the top row will all be added by 2.
 # Since my second last number in my ID is zero, it means that my starting column is zero meaning that the sliced sub-array will not effect the matrix.
 #Here is for any ID inputed
 Matrix_2 = [[5,10,15,20,25],
              [30,35,40,45,50]
    ]
 Matrix_rectangle_2 = list(Matrix_2)
 Number_of_rows = len(Matrix_rectangle_2)
 print ("The original matrix")
 for row in Matrix_rectangle_2:
     print (row)
 print("Dimensions:")
 print("Rows =", len(Matrix_rectangle_2))
 print("Columns =", len(Matrix_rectangle_2[0]))
 last_column = [row[-1] for row in Matrix_rectangle_2]
 print("Last column:", last_column)
 
 first_3_cols = [row[:3] for row in Matrix_rectangle_2]
 print("All rows with only the first 3 columns:")
 for row in first_3_cols:
     print(row)
 ID= input("Enter your student ID:")
 d_1 = ID[-1]
 d_2 = ID[-2]
 k = (int(d_1) + int(d_2))%4 +2
 shift =  int(d_1) + int(d_2)
 rows_keep = ((int(d_1))%2) +2
 row_number = d1 % Number_of_rows
 chosen_row = (int(d_1)) % len(Matrix_2)
 old_row = Matrix_rectangle_2[chosen_row][:]
 new_row = [value + k for value in old_row]
 Matrix_rectangle_2[chosen_row] = new_row
 print("The new row added by the chosen row", chosen_row,"is", new_row)
 Starting_column = (int(d_2)) % 2
 sub_array_sliced= [row[Starting_column:] for row in Matrix_rectangle_2]
 print(sub_array_sliced)
 print("\nChosen row index:", chosen_row)
 print("Old row:", old_row, "New row:", new_row)

 print("Matrix after row replacement:",Matrix_rectangle_2)

 print("Sliced sub-array from starting column", Starting_column)
 for row in sub_array_sliced:
        print(row)




if __name__ == "__main__":
    main()
