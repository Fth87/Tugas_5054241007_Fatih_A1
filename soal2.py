#berapa megawatt daya yang dihasilkan

flowRates=float(input('Enter flow rates : '))
height=float(input("Enter height : "))
mass=flowRates*1e3
gravity=9.80
#menghitung daya yang dihasilkan
power = mass*gravity*height*0.9
#convert to megawatt
power /= 1e6
print(power, "MW")