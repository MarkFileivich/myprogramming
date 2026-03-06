# Function 1: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# Function 2: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    shape = ""
    for i in range(1, rows + 1):
        shape += "*" * i + "\n"
    return shape.strip()  # Remove trailing newline at the end


# Function 3: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    num = 1
    result = ""
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip()  # Remove trailing newline at the end


# Function 4: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total


# modifications.
#  This is question 1 of the assignment
def modicheck_number():
    Number = float(input("enter a number:"))
    if Number == 0:
        print("The number is zero!")
    elif Number < 0:
        print("The number is negative!")
    elif Number > 0:
        print("the number is positive!")
# modified the return to print statements.

# input is taken as a float number so it can be any number even with decimal points
# output is zero if input is 0, number is positive if input is greater than 0 and number is negative if input is less than 0.
# This is question 2 of the assignment
def modistar_triangle():
 Number_2 = int(input("enter a number: "))
 star = ""
 for i in range (1, int(Number_2 + 1)):
    star = i*"*"
    print (star)
# removed the \n.
# The input is a integer number because we cant have half a (*)
# star is a string variable that is used to output the number of (*) as a string in rows.
# This is question 3 of the assignment
def modiIdentifying_multiples_of_3():
 Number_3 = int(input("enter a number as the limit: "))
 i = 1
 while i <= Number_3:
     if i % 3 == 0:
        print("the number is a multiple of 3")
     else:
        print(i)
     i += 1
# removed result = ""  and the results in the if and else statements.
# The input is a integer number because we dont want to have a decimal number.
# The output is one to the limit of the while loop while stating when a number is a multiple of 3 and when it is not it will print the number itself.


# This is question 4 of the assignment
def modisum_of_even_numbers_in_a_range():
 count = 0
 start = int(input("enter a starting number: "))
 end = int(input("enter an ending number: "))
 for i in range (start, end + 1):
    if i % 2 == 0:
      count += i
 print("The sum of even numbers is:", count)
# replaced return total to print count.
# The input is two integer numbers because we want the range between the numbers to be whole numbers
# The count variable is only used when i is divisiable by 2
# The count will increase by itself plus the next even i value ending with sum of all the even numbers between a given range.
if __name__ == "__main__":
    modicheck_number()
    modistar_triangle()
    modiIdentifying_multiples_of_3()
    modisum_of_even_numbers_in_a_range()
