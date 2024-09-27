x, y = map(int, input().split())
# Posisi Kenshin
posisiX, posisiY = map(int, input().split())

# Deteksi sekitar Kenshin
px1 = posisiX - 1
px2 = posisiX
px3 = posisiX + 1
px4 = posisiX
px5 = posisiX + 1
px6 = posisiX + 1
px7 = posisiX - 1
px8 = posisiX - 1

py1 = posisiY
py2 = posisiY + 1
py3 = posisiY
py4 = posisiY - 1
py5 = posisiY + 1
py6 = posisiY - 1
py7 = posisiY - 1
py8 = posisiY + 1

# Deteksi apakah melebihi ubin atau kurang dari ubin
def cekUbin(px, py):
    if (px < 0 or py < 0 or px >= x or py >= y):
        return 0
    else:
        return 1

ubin1 = cekUbin(px1, py1)
ubin2 = cekUbin(px2, py2)
ubin3 = cekUbin(px3, py3)
ubin4 = cekUbin(px4, py4)
ubin5 = cekUbin(px5, py5)
ubin6 = cekUbin(px6, py6)
ubin7 = cekUbin(px7, py7)
ubin8 = cekUbin(px8, py8)

jumlahMonster = int(input())

monsterDekat = 0

# Deteksi apakah ada monster di dekatnya
def posisiMonster(ubin, monsterX, monsterY, x, y):
    global monsterDekat
    if (ubin):
        if (monsterX == x and monsterY == y):
            monsterDekat += 1

def monster(monsterX, monsterY):
    posisiMonster(ubin1, monsterX, monsterY, px1, py1)
    posisiMonster(ubin2, monsterX, monsterY, px2, py2)
    posisiMonster(ubin3, monsterX, monsterY, px3, py3)
    posisiMonster(ubin4, monsterX, monsterY, px4, py4)
    posisiMonster(ubin5, monsterX, monsterY, px5, py5)
    posisiMonster(ubin6, monsterX, monsterY, px6, py6)
    posisiMonster(ubin7, monsterX, monsterY, px7, py7)
    posisiMonster(ubin8, monsterX, monsterY, px8, py8)

if jumlahMonster == 0:
    print('Senshi makannya besok aja deh.')
elif jumlahMonster == 1:
    monster1X, monster1Y = map(int, input().split())
    monster(monster1X, monster1Y)
elif jumlahMonster == 2:
    monster1X, monster1Y = map(int, input().split())
    monster2X, monster2Y = map(int, input().split())
    monster(monster1X, monster1Y)
    monster(monster2X, monster2Y)
elif jumlahMonster == 3:
    monster1X, monster1Y = map(int, input().split())
    monster2X, monster2Y = map(int, input().split())
    monster3X, monster3Y = map(int, input().split())
    monster(monster1X, monster1Y)
    monster(monster2X, monster2Y)
    monster(monster3X, monster3Y)
elif jumlahMonster == 4:
    monster1X, monster1Y = map(int, input().split())
    monster2X, monster2Y = map(int, input().split())
    monster3X, monster3Y = map(int, input().split())
    monster4X, monster4Y = map(int, input().split())
    monster(monster1X, monster1Y)
    monster(monster2X, monster2Y)
    monster(monster3X, monster3Y)
    monster(monster4X, monster4Y)
elif jumlahMonster == 5:
    monster1X, monster1Y = map(int, input().split())
    monster2X, monster2Y = map(int, input().split())
    monster3X, monster3Y = map(int, input().split())
    monster4X, monster4Y = map(int, input().split())
    monster5X, monster5Y = map(int, input().split())
    monster(monster1X, monster1Y)
    monster(monster2X, monster2Y)
    monster(monster3X, monster3Y)
    monster(monster4X, monster4Y)
    monster(monster5X, monster5Y)
elif jumlahMonster == 6:
    monster1X, monster1Y = map(int, input().split())
    monster2X, monster2Y = map(int, input().split())
    monster3X, monster3Y = map(int, input().split())
    monster4X, monster4Y = map(int, input().split())
    monster5X, monster5Y = map(int, input().split())
    monster6X, monster6Y = map(int, input().split())
    monster(monster1X, monster1Y)
    monster(monster2X, monster2Y)
    monster(monster3X, monster3Y)
    monster(monster4X, monster4Y)
    monster(monster5X, monster5Y)
    monster(monster6X, monster6Y)
elif jumlahMonster == 7:
    monster1X, monster1Y = map(int, input().split())
    monster2X, monster2Y = map(int, input().split())
    monster3X, monster3Y = map(int, input().split())
    monster4X, monster4Y = map(int, input().split())
    monster5X, monster5Y = map(int, input().split())
    monster6X, monster6Y = map(int, input().split())
    monster7X, monster7Y = map(int, input().split())  
    monster(monster1X, monster1Y)
    monster(monster2X, monster2Y)
    monster(monster3X, monster3Y)
    monster(monster4X, monster4Y)
    monster(monster5X, monster5Y)
    monster(monster6X, monster6Y)
    monster(monster7X, monster7Y)
elif jumlahMonster == 8:
    monster1X, monster1Y = map(int, input().split())
    monster2X, monster2Y = map(int, input().split())
    monster3X, monster3Y = map(int, input().split())
    monster4X, monster4Y = map(int, input().split())
    monster5X, monster5Y = map(int, input().split())
    monster6X, monster6Y = map(int, input().split())
    monster7X, monster7Y = map(int, input().split())
    monster8X, monster8Y = map(int, input().split())  
    monster(monster1X, monster1Y)
    monster(monster2X, monster2Y)
    monster(monster3X, monster3Y)
    monster(monster4X, monster4Y)
    monster(monster5X, monster5Y)
    monster(monster6X, monster6Y)
    monster(monster7X, monster7Y)
    monster(monster8X, monster8Y)

totalUbin = ubin1 + ubin2 + ubin3 + ubin4 + ubin5 + ubin6 + ubin7 + ubin8
# cek monster
if (monsterDekat >= totalUbin - 1):
    print('Senshi makannya besok aja deh.')
else:
    print('Senshi makan hari ini!')
