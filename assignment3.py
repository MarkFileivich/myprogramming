def main():
 import numpy as np
 import matplotlib.pyplot as plt
 # My student ID is 2582700 d1= second last digit
 d1= 0
 print("d1:", d1)
 d2 = 0
 print("d2:", d2)
 k = (d1 + d2) % 4 + 2
 print("k:", k)
 shift = (d1 - d2)
 print("shift:", shift)
 n_points = 20 + d1
 print("n_points:", n_points)
 frame_step = d2 + 1
 print("frame_step:", frame_step)
 #Component A task 1
 x= [i for i in range(1, n_points+1)]
 y= [i**2 for i in x]
 if len(x) ==0:
    print("x is empty")
 elif len(x) != len(y):
    print("x and y have different lengths")
 else:
     plt.figure(figsize=(8, 5))
     plt.plot(x,y, marker='o', linestyle='-')
     plt.title("function of x^2")
     plt.xlabel('x')
     plt.ylabel('y')
     plt.grid(True)
     plt.show()
#Component A task 2 histogram
 import random
 data_values = [random.randint(0, 30) for _ in range(30)]
 print("First 10 data values:", data_values[:10])
 if len(data_values) ==0:
        print("data_values is empty")
 else:
     plt.figure(figsize=(8, 5))
     plt.hist(data_values, bins=10, edgecolor='black')
     plt.title("Histogram of Random Data Values")
     plt.xlabel('Value Range')
     plt.ylabel('Frequency')
     plt.grid(axis='y', alpha=0.75)
     plt.show()
#This histogram shows how often a value appears which helps us see whithin a range of values for example 1-5 was repeated the most from the 30 values that were randomized with a limit of 30 being the highes possible value.
# component B Part B1
 x=[i for i in range(1, n_points+1)]
 y_2= [(i*k)+ shift for i in x]
 print("First 5 (x,y_2) pairs:", list(zip(x, y_2))[:5])
 if len(x) ==0:
    print("x is empty")
 elif len(x) != len(y_2):
     print("x and y have different lengths")
 else:
      plt.figure(figsize=(8, 5))
      plt.plot(x, y_2, marker='s', linestyle="--", color='orange')
      plt.title("x vs y2 (student ID:2582700) (k=2 shift=0)")
      plt.xlabel("x")
      plt.ylabel("y2")
      plt.grid(True)
      plt.show()
# markers are now squares and the line is dashed and orange.
# component B part B2
 x = list(range(1, n_points + 1))
 y = [i + shift for i in x]
 z = [k * i for i in x]
 print("First 5 (x, y, z) points:")
 for i in range(5):
    print(f"({x[i]}, {y[i]}, {z[i]})")
 fig = plt.figure()
 ax = fig.add_subplot(111, projection='3d')

 ax.scatter(x, y, z)


 ax.set_xlabel("X Axis")
 ax.set_ylabel("Y Axis (x + shift)")
 ax.set_zlabel("Z Axis (k * x)")

 ax.set_title("3D Scatter Plot: Linear Relationships")

 plt.show()
if __name__ == "__main__":
    main()