#Mencari posisi pada kordinat kartesius atau quadrannya

# Meminta input dari pengguna untuk koordinat x dan y
x,y = map(float, input("Enter the x and y -coordinate: ").split())

# Menentukan posisi titik pada bidang Kartesius
if x == 0 and y == 0:
    print(f"({x}, {y}) is at the origin.")
elif x == 0:
    print(f"({x}, {y}) is on the y-axis.")
elif y == 0:
    print(f"({x}, {y}) is on the x-axis.")
elif x > 0 and y > 0:
    print(f"({x}, {y}) is in quadrant I.")
elif x < 0 and y > 0:
    print(f"({x}, {y}) is in quadrant II.")
elif x < 0 and y < 0:
    print(f"({x}, {y}) is in quadrant III.")
elif x > 0 and y < 0:
    print(f"({x}, {y}) is in quadrant IV.")