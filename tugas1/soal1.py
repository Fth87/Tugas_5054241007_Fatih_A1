#menghitung biaya taksi per mile (akhir - awal)
start = float(input("Enter beggining odometer reading : "))
end = float(input("Enter ending odometer reading : "))

#menghitung biaya per mile
cost = (end - start) * 1.5
print("%.2f" %cost)

