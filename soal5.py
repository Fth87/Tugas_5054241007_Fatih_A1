#calculate VBTI(Volume to be infused) and infusion rate in ml/hr
#input
vbti = float(input("volume to be infused (ml) : "))
minutes = float(input("Minutes over which to infuse : "))

#calculate
time = 60/minutes
rate = time*vbti

print(f"vbti: {vbti:.2f} ml\nRate: {rate:.2f} ml/hr")

