#part 1: Calculate the height of the ball after time t
def calculate_height(h0, t ):
    g=9.8 # Acceleration due to gravity in m/s^2
    height=h0-0.5*g*t**2
    return round(height, 1) 

#part 2
def calculate_car_distance(t):
    speed=20
    distance=speed*t
    speed=calling_time
    return distance
if __name__ == '__main__':
    initial_height=float(input("Enter your h0 value in meters"))
    calling_time=float(input("Enter the time in seconds"))
    print ("Height of the ball at time",{calling_time}, "seconds=" ,{calculate_height(initial_height,calling_time)},"meters")
    calling_time=float(input("Enter the time in seconds"))
    print("The distance the car traveled at time",{calling_time},"seconds=",{calculate_car_distance(calling_time)},"meters")