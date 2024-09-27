X, Y = map(int,input().split())
senshix, senshiy = map(int,input().split())
Monster = int(input())

#Jika pojok
if (senshix == 0 and senshiy == 0) or (senshix == 0 and senshiy == Y) or (senshix == X and senshiy == 0) or (senshix == X and senshiy == Y):
    ubinKosong = 3

#Jika pinggir
elif(senshix == 0) or (senshiy == 0) or (senshix == X) or (senshiy == Y):
    ubinKosong = 5
    
#Jika tengah
else:
    ubinKosong = 8

#function untuk mengecek apakah monster ada di Sekitar Senshi??
def cekApakahSebelahanSamaMonster(posisiMonsterX,posisiMonsterY):
    global ubinKosong
    if (senshix+1 == posisiMonsterX or senshix-1 == posisiMonsterX) or (senshiy+1 == posisiMonsterY or senshiy-1 == posisiMonsterY):
        ubinKosong -= 1

#Cek sesuai jumlah monster
if Monster >= 1:
    posisiMonster1X, posisiMonster1Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster1X,posisiMonster1Y)
if Monster >= 2:
    posisiMonster2X, posisiMonster2Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster2X,posisiMonster2Y)
if Monster >= 3:
    posisiMonster3X, posisiMonster3Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster3X,posisiMonster3Y)
if Monster >= 4:
    posisiMonster4X, posisiMonster4Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster4X,posisiMonster4Y)
if Monster >= 5:
    posisiMonster5X, posisiMonster5Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster5X,posisiMonster5Y)
if Monster >= 6:
    posisiMonster6X, posisiMonster6Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster6X,posisiMonster6Y)
if Monster >= 7:
    posisiMonster7X, posisiMonster7Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster7X,posisiMonster7Y)
if Monster >= 8:
    posisiMonster8X, posisiMonster8Y = map(int,input().split())
    cekApakahSebelahanSamaMonster(posisiMonster8X,posisiMonster8Y)
if Monster == 0:
    ubinKosong = 0
    
print("Senshi makan hari ini!") if ubinKosong > 0 else print("Senshi makannya besok aja deh.")
