#Student ID: 2582700
#d1 = 0
#d2 = 0
#k= (0+0) % 4 + 2 =2
#shift = 0-0 = 0
#rows_keep = (0%2) +2 =2
#component A
def main():
 num_readings = int(input("Enter how many readings (number) will you enter:"))
 inputed_readings = []

 for i in range(num_readings):
    reading = float(input(f"Enter reading {i+1}:"))
    inputed_readings.append(reading)
 if len(inputed_readings) > 0:
    print ("full list",inputed_readings)
    print ("first reading is:",inputed_readings[0])
    print ("last reading is:",inputed_readings[-1])
 else:
    print ("No readings were entered so list is empty")
 if len(inputed_readings) >= 4:
    print ("The slice from index 1 to index 3 is:", inputed_readings[1:4])
 else:
    print ("Not enough readings to slice from index 1 to index 3")
 # component B
 d1=0
 d2=0
 k=(d1+d2) % 4 +2 
 shift= d1-d2
 rows_keep= (d1%2) + 2 
 List_1  = [x for x in inputed_readings]
 shifted = [ x + shift for x in List_1]
 print ("New readings after adding shift:", shifted)
 third_list = [ x * k for x in List_1]
 print ("New readings after multiplying by k:", third_list)
 sum_list = [ a + b for a, b in zip (List_1, shifted)]
 print ("list after adding list 1 and shifted:", sum_list)
#proof that zip() still works of list lengths that do not match
 First_list=[3,4,5]
 Second_list=[7,6,5,4,3]
 total_list= [c+d for c,d in zip(First_list,Second_list) ]
 print("The sum of the first list with the second list is:", total_list)


if __name__=="__main__":
 main()
