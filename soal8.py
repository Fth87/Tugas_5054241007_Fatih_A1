#estimate the magnitude (liters/day) and cost of the water saved based on the community population

#1 toilet every 3 persons
#avg 14 times flush per day 
#15 liter per flush
#input = community population

population = int(input("community population : "))
toilet = population/3
flush = 15
avgFlush = 14

magnitude = flush * avgFlush * toilet

print(f"estimate magnitude : {magnitude} liters/day")







