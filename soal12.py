#calculate the acceleration(m/s^2) of a jet fighter launched

velocity = float(input("jet velocity : "))
distance = float(input("distance : "))


time = (2*distance)/velocity
acceleration = velocity/time

print(f"acceleration: {acceleration:.2f} m/s^2")


