x1, y1 = map(int, input().split())  
xs, ys = map(int, input().split())
xf, yf = map(int, input().split()) 

jarak_king = (xs - xf)**2 + (ys - yf)**2

jarak_lingkaran_ke_akhir = (x1 - xf)**2 + (y1 - yf)**2

#kan semakin gede jarake otomatis semakin suwi kan tekan kono
#nah berati nak rajane meh neng titik akhir dg selamat, jarake kudu lweh  pendek daripada lingkaran seng ngejar dee

if int(jarak_lingkaran_ke_akhir) > int(jarak_king):
    print("Yes")
else:
    print("No")