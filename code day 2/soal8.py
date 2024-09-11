#Menghitung service kendaraan

print(" (1) First Free Service ")
print(" (2) Second Free Service ")
number = input("Enter the free service number >> ")
miles = input("Enter number of Miles >> ")

if(number == 1):
    if(1500 < miles <=3000):
        print("Vehicle must be serviced")
    else:
        print("Vehicle is not required for this free service.")
elif(number == 2):
    if(3001 < number <= 4500):
        print("Vehicle must be serviced")
    else:
        print("Vehicle is not required for this free service.")


