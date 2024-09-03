#how many btu heat are delivered to house

efficiency = float(input("efficiency : "))
gallons = float(input("gallons : "))

efficiency /= 100
barrel = gallons/42
barrel *= 5800000

totalBTU = barrel * efficiency;

print(f"{totalBTU:.2f} BTU")
