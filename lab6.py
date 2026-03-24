#Lab 6
ID = 2582700
d1 = 0
d2 = 0
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2
#part 1
def main():
 Temperature = [[21, 22, 23, 24],
          [25, 26, 27, 28],
          [29, 30, 31, 32]
 ]
 
 print (Temperature,"Original Temperatures")
 print ("The value in the second row and fourth collum is:", Temperature[1][3])
 print ("The first two rows are:", Temperature [:2])
 first_column = [row[0] for row in Temperature]
 print ("The first column is:", first_column)
 sub_array = [row[:2]for row in Temperature[:2]]
 print ("the sub-array 2x2 from the upper-left corner is:", sub_array)
 #Component B
 #made it so i can input any ID
 #My ID is 2582700.
 ID = (input("Enter your student ID:"))
 d1=ID [-1]
 d2=ID [-2]
 k= (int(d1)+int(d2)) % 4 + 2
 shift = int(d1)-int(d2)
 rows_keep = (int(d1)% 2) +2
 # the %3 represents the 3 rows
 Number_of_rows= (int(d1)) % 3
 # the % 4 represents th number of columns
 Number_of_column= (int(d2)) % 4
 Temperature[Number_of_rows] = [value + shift for value in Temperature [Number_of_rows]]
 print("The row being added by shift is:",Temperature[Number_of_rows] )
 for i in range(len(Temperature)):
    Temperature[i][Number_of_column] *= k 
 column_values = [row[Number_of_column] for row in Temperature]
 print("The column after multiplying by k is:", column_values)
 sub_array =[row[:k] for row in Temperature[:rows_keep]]
 print ("The sub_array using first rows_keep and first k colomns is:")
 for row in sub_array:
    print(row)
 print ("The new Temperatures are:", Temperature)
if __name__ == "__main__":
   main()