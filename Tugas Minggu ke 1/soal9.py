#time required to cut grass in (house - yard)
#time = 2feet^2/ second

yard = list(map(float,input("length and width in yard : ").split()))
house = list(map(float,input("length and width in house : ").split()))

yard = yard[0]*yard[1]*9
house = house[0]*house[1]  *9  

grass = yard - house
time = grass/2  

print(f"{time:.2f} seconds")



