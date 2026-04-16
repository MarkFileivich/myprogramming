def main():
 import numpy as np
 import matplotlib.pyplot as plt
 # Question 1
 x = [1,2,3,4,5]
 y = [1,4,9,16,25]
 plt.plot(x, y, marker='o', linestyle='-')
 plt.title("Curved plot")
 plt.xlabel("X-axis")
 plt.ylabel("Y-axis")
 plt.grid(True)
 plt.show()
 # cos function graph since its a curved plot.
 x = np.linspace(0, 10, 100)
 y = np.cos(x)
 plt.plot(x, y, marker='o', linestyle='-')
 plt.title("Curved plot of cos function")
 plt.xlabel("X-axis")
 plt.ylabel("Y-axis")
 plt.grid(True)
 plt.show()
 # Question 2
 Temperature = [9000,8000, 7000, 5000, 3000]
 luminosity = [1000.0, 500, 150.0, 100.0, 50.0]
 plt.scatter(Temperature, luminosity, c=Temperature, cmap='viridis', edgecolors='b')
 plt.title("Hertzsprung-Russell Diagram")
 plt.gca().invert_xaxis()
 plt.xlabel("Temperature (K)")
 plt.ylabel("Luminosity (Lâ˜‰)")
 plt.colorbar(label="Temperature (K)")
 plt.show()
 # Question 3 Density plot.
 np.random.seed(0)
 data = np.random.rand(1000, 2)
 color_map = plt.cm.viridis
 plt.hist2d(data[:, 0], data[:, 1], bins=50, cmap='gray', density=True)
 plt.colorbar(label='Density')
 plt.xlabel("X-axis")
 plt.ylabel("Y-axis")
 plt.title("Density Plot")
 plt.show()

if __name__ == "__main__":
    main()
