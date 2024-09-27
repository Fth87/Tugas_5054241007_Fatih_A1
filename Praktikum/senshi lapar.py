x,y = map(int,input().split())

# Posisi kenshin
posisiX,posisiY = map(int,input().split())

#deteksi sekitar kensin
px1=posisiX-1
px2=posisiX
px3=posisiX+1
px4=posisiX
px5=posisiX+1
px6=posisiX+1
px7=posisiX-1
px8=posisiX-1

py1=posisiY
py2=posisiY+1
py3=posisiY
py4=posisiY-1
py5=posisiY+1
py6=posisiY-1
py7=posisiY-1
py8=posisiY+1





#Deteksi apakah melebihi ubin atau kurang dari ubin
#Cek ubin pertama
ubin1=1
if(px1 < 0 or py1 < 0 or px1 >= x or py1 >= y):
    ubin1=0
    
#Cek ubin kedua
ubin2=1
if(px2 < 0 or py2 < 0 or px2 >= x or py2 >= y):
    ubin2=0
    
    
#Cek ubin ketiga
ubin3=1
if(px3 < 0 or py3 < 0 or px3 >= x or py3 >= y):
    ubin3=0

#Cek ubin keempat
ubin4=1
if(px4 < 0 or py4 < 0 or px4 >= x or py4 >= y):
    ubin4=0
    
#Cek ubin kelima
ubin5=1
if(px5 < 0 or py5 < 0 or px5 >= x or py5 >= y):
    ubin5=0
    
#Cek ubin keenam
ubin6=1
if(px6 < 0 or py6 < 0 or px6 >= x or py6 >= y):
    ubin6=0
    
#Cek ubin ketujuh
ubin7=1
if(px7 < 0 or py7 < 0 or px7 >= x or py7 >= y):
    ubin7=0
    
#Cek ubin kedelapan 
ubin8=1
if(px8 < 0 or py8 < 0 or px8 >= x or py8 >= y):
    ubin8=0
    

jumlahMonster = int(input())

#posisi monster

if(jumlahMonster==0):
    print('Senshi makannya besok aja deh.')
    
    #________________________________________________________________________Monster 1_____________________________________________
elif(jumlahMonster==1):
    monster1X,monster1Y =  map(int,input().split())
    #deteksi monster jika monster 1
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1

    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
    #________________________________________________________________________Monster 2_____________________________________________
elif (jumlahMonster == 2 ):
    monster1X,monster1Y =  map(int,input().split())
    monster2X,monster2Y =  map(int,input().split())  
    #deteksi monster
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
        #Cek monster kedua di ubin 1
        if(monster2X == px1 and monster2Y == py1):
            monsterDekat+=1

    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
        #Cek monster kedua di ubin2
        if(monster2X == px2 and monster2Y == py2):
            monsterDekat+=1
        
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
        #Cek monster kedua di ubin3
        if(monster2X == px3 and monster2Y == py3):
            monsterDekat+=1  

    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1
        #cek monster kedua di ubin4
        if(monster2X == px4 and monster2Y == py4):
            monsterDekat+=1


    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
        #cek monster kedua di ubin5
        if(monster2X == px5 and monster2Y == py5):
            monsterDekat+=1

    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
        #cek monster kedua di ubin6
        if(monster2X == px6 and monster2Y == py6):
            monsterDekat+=1

    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
        #cek monster kedua di ubin7
        if(monster2X == px7 and monster2Y == py7):
            monsterDekat+=1

    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
        #cek monster kedua di ubin8
        if(monster2X == px8 and monster2Y == py8):
            monsterDekat+=1
    #________________________________________________________________________Monster 3_____________________________________________
elif (jumlahMonster == 3 ):
    monster1X,monster1Y =  map(int,input().split())
    monster2X,monster2Y =  map(int,input().split())
    monster3X,monster3Y =  map(int,input().split())
    #deteksi monster
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
        #Cek monster kedua di ubin 1
        if(monster2X == px1 and monster2Y == py1):
            monsterDekat+=1
        #Cek monster ketiga di ubin 1
        if(monster3X == px1 and monster3Y == py1):
            monsterDekat+=1

    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
        #Cek monster kedua di ubin2
        if(monster2X == px2 and monster2Y == py2):
            monsterDekat+=1
        #Cek monster ketiga di ubin 2
        if(monster3X == px2 and monster3Y == py2):
            monsterDekat+=1
        
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
        #Cek monster kedua di ubin3
        if(monster2X == px3 and monster2Y == py3):
            monsterDekat+=1  
        #Cek monster ketiga di ubin 3
        if(monster3X == px3 and monster3Y == py3):
            monsterDekat+=1
    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1
        #cek monster kedua di ubin4
        if(monster2X == px4 and monster2Y == py4):
            monsterDekat+=1
        #cek monster ketiga di ubin 4
        if(monster3X == px4 and monster3Y == py4):
            monsterDekat+=1

    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
        #cek monster kedua di ubin5
        if(monster2X == px5 and monster2Y == py5):
            monsterDekat+=1
        #cek monster ketiga di ubin5    
        if(monster3X == px5 and monster3Y == py5):
            monsterDekat+=1
    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
        #cek monster kedua di ubin6
        if(monster2X == px6 and monster2Y == py6):
            monsterDekat+=1
        #cek monster ketiga di ubin6
        if(monster3X == px6 and monster3Y == py6):
            monsterDekat+=1
    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
        #cek monster kedua di ubin7
        if(monster2X == px7 and monster2Y == py7):
            monsterDekat+=1
        #cek monster ketiga di ubin7
        if(monster3X == px7 and monster3Y == py7):
            monsterDekat+=1
    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
        #cek monster kedua di ubin8
        if(monster2X == px8 and monster2Y == py8):
            monsterDekat+=1
        #cek monster ketiga di ubin8
        if(monster3X == px8 and monster3Y == py8):
            monsterDekat+=1
  #________________________________________________________________________Monster 4_____________________________________________
elif (jumlahMonster == 4 ):
    monster1X,monster1Y =  map(int,input().split())
    monster2X,monster2Y =  map(int,input().split())
    monster3X,monster3Y =  map(int,input().split())
    monster4X,monster4Y =  map(int,input().split())
    #deteksi monster
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
        #Cek monster kedua di ubin 1
        if(monster2X == px1 and monster2Y == py1):
            monsterDekat+=1
        #Cek monster ketiga di ubin 1
        if(monster3X == px1 and monster3Y == py1):
            monsterDekat+=1
        #Cek monster keempat di ubin 1
        if(monster4X == px1 and monster4Y == py1):
            monsterDekat+=1

    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
        #Cek monster kedua di ubin2
        if(monster2X == px2 and monster2Y == py2):
            monsterDekat+=1
        #Cek monster ketiga di ubin 2
        if(monster3X == px2 and monster3Y == py2):
            monsterDekat+=1
        #Cek monster keempat di ubin 2
        if(monster4X == px2 and monster4Y == py2):
            monsterDekat+=1
        
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
        #Cek monster kedua di ubin3
        if(monster2X == px3 and monster2Y == py3):
            monsterDekat+=1  
        #Cek monster ketiga di ubin 3
        if(monster3X == px3 and monster3Y == py3):
            monsterDekat+=1
        #Cek monster keempat di ubin 3
        if(monster4X == px3 and monster4Y == py3):
            monsterDekat+=1
            
    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1
        #cek monster kedua di ubin4
        if(monster2X == px4 and monster2Y == py4):
            monsterDekat+=1
        #cek monster ketiga di ubin 4
        if(monster3X == px4 and monster3Y == py4):
            monsterDekat+=1
        #cek monster keempat di ubin 4
        if(monster4X == px4 and monster4Y == py4):
            monsterDekat+=1

    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
        #cek monster kedua di ubin5
        if(monster2X == px5 and monster2Y == py5):
            monsterDekat+=1
        #cek monster ketiga di ubin5    
        if(monster3X == px5 and monster3Y == py5):
            monsterDekat+=1
        #cek monster keempat di ubin5    
        if(monster4X == px5 and monster4Y == py5):
            monsterDekat+=1
    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
        #cek monster kedua di ubin6
        if(monster2X == px6 and monster2Y == py6):
            monsterDekat+=1
        #cek monster ketiga di ubin6
        if(monster3X == px6 and monster3Y == py6):
            monsterDekat+=1
        #cek monster keempat di ubin6
        if(monster4X == px6 and monster4Y == py6):
            monsterDekat+=1
    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
        #cek monster kedua di ubin7
        if(monster2X == px7 and monster2Y == py7):
            monsterDekat+=1
        #cek monster ketiga di ubin7
        if(monster3X == px7 and monster3Y == py7):
            monsterDekat+=1
        #cek monster keempat di ubin7
        if(monster4X == px7 and monster4Y == py7):
            monsterDekat+=1
    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
        #cek monster kedua di ubin8
        if(monster2X == px8 and monster2Y == py8):
            monsterDekat+=1
        #cek monster ketiga di ubin8
        if(monster3X == px8 and monster3Y == py8):
            monsterDekat+=1
        #cek monster keempat di ubin8
        if(monster4X == px8 and monster4Y == py8):
            monsterDekat+=1
  #________________________________________________________________________Monster 5_____________________________________________
elif (jumlahMonster == 5 ):
    monster1X,monster1Y =  map(int,input().split())
    monster2X,monster2Y =  map(int,input().split())
    monster3X,monster3Y =  map(int,input().split())
    monster4X,monster4Y =  map(int,input().split())
    monster5X,monster5Y =  map(int,input().split())
    #deteksi monster
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
        #Cek monster kedua di ubin 1
        if(monster2X == px1 and monster2Y == py1):
            monsterDekat+=1
        #Cek monster ketiga di ubin 1
        if(monster3X == px1 and monster3Y == py1):
            monsterDekat+=1
        #Cek monster keempat di ubin 1
        if(monster4X == px1 and monster4Y == py1):
            monsterDekat+=1
        #Cek monster lima di ubin 1
        if(monster5X == px1 and monster5Y == py1):
            monsterDekat+=1

    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
        #Cek monster kedua di ubin2
        if(monster2X == px2 and monster2Y == py2):
            monsterDekat+=1
        #Cek monster ketiga di ubin 2
        if(monster3X == px2 and monster3Y == py2):
            monsterDekat+=1
        #Cek monster keempat di ubin 2
        if(monster4X == px2 and monster4Y == py2):
            monsterDekat+=1
        #Cek monster kelima di ubin 2
        if(monster5X == px2 and monster5Y == py2):
            monsterDekat+=1
        
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
        #Cek monster kedua di ubin3
        if(monster2X == px3 and monster2Y == py3):
            monsterDekat+=1  
        #Cek monster ketiga di ubin 3
        if(monster3X == px3 and monster3Y == py3):
            monsterDekat+=1
        #Cek monster keempat di ubin 3
        if(monster4X == px3 and monster4Y == py3):
            monsterDekat+=1
        #Cek monster keelima di ubin 3
        if(monster5X == px3 and monster5Y == py3):
            monsterDekat+=1
            
    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1
        #cek monster kedua di ubin4
        if(monster2X == px4 and monster2Y == py4):
            monsterDekat+=1
        #cek monster ketiga di ubin 4
        if(monster3X == px4 and monster3Y == py4):
            monsterDekat+=1
        #cek monster keempat di ubin 4
        if(monster4X == px4 and monster4Y == py4):
            monsterDekat+=1
        #cek monster kelima di ubin 4
        if(monster5X == px4 and monster5Y == py4):
            monsterDekat+=1

    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
        #cek monster kedua di ubin5
        if(monster2X == px5 and monster2Y == py5):
            monsterDekat+=1
        #cek monster ketiga di ubin5    
        if(monster3X == px5 and monster3Y == py5):
            monsterDekat+=1
        #cek monster keempat di ubin5    
        if(monster4X == px5 and monster4Y == py5):
            monsterDekat+=1
        #cek monster klima di ubin5    
        if(monster5X == px5 and monster5Y == py5):
            monsterDekat+=1
    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
        #cek monster kedua di ubin6
        if(monster2X == px6 and monster2Y == py6):
            monsterDekat+=1
        #cek monster ketiga di ubin6
        if(monster3X == px6 and monster3Y == py6):
            monsterDekat+=1
        #cek monster keempat di ubin6
        if(monster4X == px6 and monster4Y == py6):
            monsterDekat+=1
        #cek monster kelima di ubin6
        if(monster5X == px6 and monster5Y == py6):
            monsterDekat+=1
    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
        #cek monster kedua di ubin7
        if(monster2X == px7 and monster2Y == py7):
            monsterDekat+=1
        #cek monster ketiga di ubin7
        if(monster3X == px7 and monster3Y == py7):
            monsterDekat+=1
        #cek monster keempat di ubin7
        if(monster4X == px7 and monster4Y == py7):
            monsterDekat+=1
        #cek monster kelima di ubin7
        if(monster5X == px7 and monster5Y == py7):
            monsterDekat+=1
    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
        #cek monster kedua di ubin8
        if(monster2X == px8 and monster2Y == py8):
            monsterDekat+=1
        #cek monster ketiga di ubin8
        if(monster3X == px8 and monster3Y == py8):
            monsterDekat+=1
        #cek monster keempat di ubin8
        if(monster4X == px8 and monster4Y == py8):
            monsterDekat+=1
        #cek monster kelima di ubin8
        if(monster5X == px8 and monster5Y == py8):
            monsterDekat+=1
  #________________________________________________________________________Monster 6_____________________________________________
elif (jumlahMonster == 6 ):
    monster1X,monster1Y =  map(int,input().split())
    monster2X,monster2Y =  map(int,input().split())
    monster3X,monster3Y =  map(int,input().split())
    monster4X,monster4Y =  map(int,input().split())
    monster5X,monster5Y =  map(int,input().split())
    monster6X,monster6Y =  map(int,input().split())
    #deteksi monster
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
        #Cek monster kedua di ubin 1
        if(monster2X == px1 and monster2Y == py1):
            monsterDekat+=1
        #Cek monster ketiga di ubin 1
        if(monster3X == px1 and monster3Y == py1):
            monsterDekat+=1
        #Cek monster keempat di ubin 1
        if(monster4X == px1 and monster4Y == py1):
            monsterDekat+=1
        #Cek monster lima di ubin 1
        if(monster5X == px1 and monster5Y == py1):
            monsterDekat+=1
        #Cek monster enam di ubin 1
        if(monster6X == px1 and monster6Y == py1):
            monsterDekat+=1

    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
        #Cek monster kedua di ubin2
        if(monster2X == px2 and monster2Y == py2):
            monsterDekat+=1
        #Cek monster ketiga di ubin 2
        if(monster3X == px2 and monster3Y == py2):
            monsterDekat+=1
        #Cek monster keempat di ubin 2
        if(monster4X == px2 and monster4Y == py2):
            monsterDekat+=1
        #Cek monster kelima di ubin 2
        if(monster5X == px2 and monster5Y == py2):
            monsterDekat+=1
        #Cek monster keenam di ubin 2
        if(monster6X == px2 and monster6Y == py2):
            monsterDekat+=1
        
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
        #Cek monster kedua di ubin3
        if(monster2X == px3 and monster2Y == py3):
            monsterDekat+=1  
        #Cek monster ketiga di ubin 3
        if(monster3X == px3 and monster3Y == py3):
            monsterDekat+=1
        #Cek monster keempat di ubin 3
        if(monster4X == px3 and monster4Y == py3):
            monsterDekat+=1
        #Cek monster keelima di ubin 3
        if(monster5X == px3 and monster5Y == py3):
            monsterDekat+=1
        #Cek monster keenam di ubin 3
        if(monster6X == px3 and monster6Y == py3):
            monsterDekat+=1
            
    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1
        #cek monster kedua di ubin4
        if(monster2X == px4 and monster2Y == py4):
            monsterDekat+=1
        #cek monster ketiga di ubin 4
        if(monster3X == px4 and monster3Y == py4):
            monsterDekat+=1
        #cek monster keempat di ubin 4
        if(monster4X == px4 and monster4Y == py4):
            monsterDekat+=1
        #cek monster kelima di ubin 4
        if(monster5X == px4 and monster5Y == py4):
            monsterDekat+=1
        #cek monster keenam di ubin 4
        if(monster6X == px4 and monster6Y == py4):
            monsterDekat+=1

    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
        #cek monster kedua di ubin5
        if(monster2X == px5 and monster2Y == py5):
            monsterDekat+=1
        #cek monster ketiga di ubin5    
        if(monster3X == px5 and monster3Y == py5):
            monsterDekat+=1
        #cek monster keempat di ubin5    
        if(monster4X == px5 and monster4Y == py5):
            monsterDekat+=1
        #cek monster klima di ubin5    
        if(monster5X == px5 and monster5Y == py5):
            monsterDekat+=1
        #cek monster keenam di ubin5    
        if(monster6X == px5 and monster6Y == py5):
            monsterDekat+=1
    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
        #cek monster kedua di ubin6
        if(monster2X == px6 and monster2Y == py6):
            monsterDekat+=1
        #cek monster ketiga di ubin6
        if(monster3X == px6 and monster3Y == py6):
            monsterDekat+=1
        #cek monster keempat di ubin6
        if(monster4X == px6 and monster4Y == py6):
            monsterDekat+=1
        #cek monster kelima di ubin6
        if(monster5X == px6 and monster5Y == py6):
            monsterDekat+=1
        #cek monster keenam di ubin6
        if(monster6X == px6 and monster6Y == py6):
            monsterDekat+=1
    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
        #cek monster kedua di ubin7
        if(monster2X == px7 and monster2Y == py7):
            monsterDekat+=1
        #cek monster ketiga di ubin7
        if(monster3X == px7 and monster3Y == py7):
            monsterDekat+=1
        #cek monster keempat di ubin7
        if(monster4X == px7 and monster4Y == py7):
            monsterDekat+=1
        #cek monster kelima di ubin7
        if(monster5X == px7 and monster5Y == py7):
            monsterDekat+=1
        #cek monster keenam di ubin7
        if(monster6X == px7 and monster6Y == py7):
            monsterDekat+=1
    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
        #cek monster kedua di ubin8
        if(monster2X == px8 and monster2Y == py8):
            monsterDekat+=1
        #cek monster ketiga di ubin8
        if(monster3X == px8 and monster3Y == py8):
            monsterDekat+=1
        #cek monster keempat di ubin8
        if(monster4X == px8 and monster4Y == py8):
            monsterDekat+=1
        #cek monster kelima di ubin8
        if(monster5X == px8 and monster5Y == py8):
            monsterDekat+=1
        #cek monster keenam di ubin8
        if(monster6X == px8 and monster6Y == py8):
            monsterDekat+=1
  #________________________________________________________________________Monster 7_____________________________________________
elif (jumlahMonster == 7 ):
    monster1X,monster1Y =  map(int,input().split())
    monster2X,monster2Y =  map(int,input().split())
    monster3X,monster3Y =  map(int,input().split())
    monster4X,monster4Y =  map(int,input().split())
    monster5X,monster5Y =  map(int,input().split())
    monster6X,monster6Y =  map(int,input().split())
    monster7X,monster7Y =  map(int,input().split())
    #deteksi monster
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
        #Cek monster kedua di ubin 1
        if(monster2X == px1 and monster2Y == py1):
            monsterDekat+=1
        #Cek monster ketiga di ubin 1
        if(monster3X == px1 and monster3Y == py1):
            monsterDekat+=1
        #Cek monster keempat di ubin 1
        if(monster4X == px1 and monster4Y == py1):
            monsterDekat+=1
        #Cek monster lima di ubin 1
        if(monster5X == px1 and monster5Y == py1):
            monsterDekat+=1
        #Cek monster enam di ubin 1
        if(monster6X == px1 and monster6Y == py1):
            monsterDekat+=1
        #Cek monster ketujuh di ubin 1
        if(monster7X == px1 and monster7Y == py1):
            monsterDekat+=1

    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
        #Cek monster kedua di ubin2
        if(monster2X == px2 and monster2Y == py2):
            monsterDekat+=1
        #Cek monster ketiga di ubin 2
        if(monster3X == px2 and monster3Y == py2):
            monsterDekat+=1
        #Cek monster keempat di ubin 2
        if(monster4X == px2 and monster4Y == py2):
            monsterDekat+=1
        #Cek monster kelima di ubin 2
        if(monster5X == px2 and monster5Y == py2):
            monsterDekat+=1
        #Cek monster keenam di ubin 2
        if(monster6X == px2 and monster6Y == py2):
            monsterDekat+=1
        #Cek monster ketujuh di ubin 2
        if(monster7X == px2 and monster7Y == py2):
            monsterDekat+=1
        
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
        #Cek monster kedua di ubin3
        if(monster2X == px3 and monster2Y == py3):
            monsterDekat+=1  
        #Cek monster ketiga di ubin 3
        if(monster3X == px3 and monster3Y == py3):
            monsterDekat+=1
        #Cek monster keempat di ubin 3
        if(monster4X == px3 and monster4Y == py3):
            monsterDekat+=1
        #Cek monster keelima di ubin 3
        if(monster5X == px3 and monster5Y == py3):
            monsterDekat+=1
        #Cek monster keenam di ubin 3
        if(monster6X == px3 and monster6Y == py3):
            monsterDekat+=1
        #Cek monster ketujuh di ubin 3
        if(monster7X == px3 and monster7Y == py3):
            monsterDekat+=1
            
    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1
        #cek monster kedua di ubin4
        if(monster2X == px4 and monster2Y == py4):
            monsterDekat+=1
        #cek monster ketiga di ubin 4
        if(monster3X == px4 and monster3Y == py4):
            monsterDekat+=1
        #cek monster keempat di ubin 4
        if(monster4X == px4 and monster4Y == py4):
            monsterDekat+=1
        #cek monster kelima di ubin 4
        if(monster5X == px4 and monster5Y == py4):
            monsterDekat+=1
        #cek monster keenam di ubin 4
        if(monster6X == px4 and monster6Y == py4):
            monsterDekat+=1
        #cek monster ketujuh di ubin 4
        if(monster7X == px4 and monster7Y == py4):
            monsterDekat+=1

    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
        #cek monster kedua di ubin5
        if(monster2X == px5 and monster2Y == py5):
            monsterDekat+=1
        #cek monster ketiga di ubin5    
        if(monster3X == px5 and monster3Y == py5):
            monsterDekat+=1
        #cek monster keempat di ubin5    
        if(monster4X == px5 and monster4Y == py5):
            monsterDekat+=1
        #cek monster klima di ubin5    
        if(monster5X == px5 and monster5Y == py5):
            monsterDekat+=1
        #cek monster keenam di ubin5    
        if(monster6X == px5 and monster6Y == py5):
            monsterDekat+=1
        #cek monster ketujuh di ubin5    
        if(monster7X == px5 and monster7Y == py5):
            monsterDekat+=1
            
    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
        #cek monster kedua di ubin6
        if(monster2X == px6 and monster2Y == py6):
            monsterDekat+=1
        #cek monster ketiga di ubin6
        if(monster3X == px6 and monster3Y == py6):
            monsterDekat+=1
        #cek monster keempat di ubin6
        if(monster4X == px6 and monster4Y == py6):
            monsterDekat+=1
        #cek monster kelima di ubin6
        if(monster5X == px6 and monster5Y == py6):
            monsterDekat+=1
        #cek monster keenam di ubin6
        if(monster6X == px6 and monster6Y == py6):
            monsterDekat+=1
        #cek monster ketujuh di ubin6
        if(monster7X == px6 and monster7Y == py6):
            monsterDekat+=1
            
    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
        #cek monster kedua di ubin7
        if(monster2X == px7 and monster2Y == py7):
            monsterDekat+=1
        #cek monster ketiga di ubin7
        if(monster3X == px7 and monster3Y == py7):
            monsterDekat+=1
        #cek monster keempat di ubin7
        if(monster4X == px7 and monster4Y == py7):
            monsterDekat+=1
        #cek monster kelima di ubin7
        if(monster5X == px7 and monster5Y == py7):
            monsterDekat+=1
        #cek monster keenam di ubin7
        if(monster6X == px7 and monster6Y == py7):
            monsterDekat+=1
            
        #cek monster ketujuh di ubin7
        if(monster7X == px7 and monster7Y == py7):
            monsterDekat+=1
            
    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
        #cek monster kedua di ubin8
        if(monster2X == px8 and monster2Y == py8):
            monsterDekat+=1
        #cek monster ketiga di ubin8
        if(monster3X == px8 and monster3Y == py8):
            monsterDekat+=1
        #cek monster keempat di ubin8
        if(monster4X == px8 and monster4Y == py8):
            monsterDekat+=1
        #cek monster kelima di ubin8
        if(monster5X == px8 and monster5Y == py8):
            monsterDekat+=1
        #cek monster keenam di ubin8
        if(monster6X == px8 and monster6Y == py8):
            monsterDekat+=1
        #cek monster ketujuh di ubin8
        if(monster7X == px8 and monster7Y == py8):
            monsterDekat+=1
  #________________________________________________________________________Monster 7_____________________________________________
elif (jumlahMonster == 8 ):
    monster1X,monster1Y =  map(int,input().split())
    monster2X,monster2Y =  map(int,input().split())
    monster3X,monster3Y =  map(int,input().split())
    monster4X,monster4Y =  map(int,input().split())
    monster5X,monster5Y =  map(int,input().split())
    monster6X,monster6Y =  map(int,input().split())
    monster7X,monster7Y =  map(int,input().split())
    monster8X,monster8Y =  map(int,input().split())
    #deteksi monster
    monsterDekat = 0
    if(ubin1):
        #Cek monster pertama di ubin1
        if(monster1X == px1 and monster1Y == py1):
            monsterDekat+=1
        #Cek monster kedua di ubin 1
        if(monster2X == px1 and monster2Y == py1):
            monsterDekat+=1
        #Cek monster ketiga di ubin 1
        if(monster3X == px1 and monster3Y == py1):
            monsterDekat+=1
        #Cek monster keempat di ubin 1
        if(monster4X == px1 and monster4Y == py1):
            monsterDekat+=1
        #Cek monster lima di ubin 1
        if(monster5X == px1 and monster5Y == py1):
            monsterDekat+=1
        #Cek monster enam di ubin 1
        if(monster6X == px1 and monster6Y == py1):
            monsterDekat+=1
        #Cek monster ketujuh di ubin 1
        if(monster7X == px1 and monster7Y == py1):
            monsterDekat+=1
        #Cek monster delapan di ubin 1
        if(monster8X == px1 and monster8Y == py1):
            monsterDekat+=1

    if(ubin2):
        #Cek monster pertama di ubin2
        if(monster1X == px2 and monster1Y == py2):
            monsterDekat+=1
        #Cek monster kedua di ubin2
        if(monster2X == px2 and monster2Y == py2):
            monsterDekat+=1
        #Cek monster ketiga di ubin 2
        if(monster3X == px2 and monster3Y == py2):
            monsterDekat+=1
        #Cek monster keempat di ubin 2
        if(monster4X == px2 and monster4Y == py2):
            monsterDekat+=1
        #Cek monster kelima di ubin 2
        if(monster5X == px2 and monster5Y == py2):
            monsterDekat+=1
        #Cek monster keenam di ubin 2
        if(monster6X == px2 and monster6Y == py2):
            monsterDekat+=1
        #Cek monster ketujuh di ubin 2
        if(monster7X == px2 and monster7Y == py2):
            monsterDekat+=1
        #Cek monster kedelapan di ubin 2
        if(monster8X == px2 and monster8Y == py2):
            monsterDekat+=1
        
    if(ubin3):
    #Cek monster pertama di ubin3
        if(monster1X == px3 and monster1Y == py3):
            monsterDekat+=1  
        #Cek monster kedua di ubin3
        if(monster2X == px3 and monster2Y == py3):
            monsterDekat+=1  
        #Cek monster ketiga di ubin 3
        if(monster3X == px3 and monster3Y == py3):
            monsterDekat+=1
        #Cek monster keempat di ubin 3
        if(monster4X == px3 and monster4Y == py3):
            monsterDekat+=1
        #Cek monster keelima di ubin 3
        if(monster5X == px3 and monster5Y == py3):
            monsterDekat+=1
        #Cek monster keenam di ubin 3
        if(monster6X == px3 and monster6Y == py3):
            monsterDekat+=1
        #Cek monster ketujuh di ubin 3
        if(monster7X == px3 and monster7Y == py3):
            monsterDekat+=1
        #Cek monster kedelapan di ubin 3
        if(monster8X == px3 and monster8Y == py3):
            monsterDekat+=1
            
    if(ubin4):
        #cek monster pertama di ubin4
        if(monster1X == px4 and monster1Y == py4):
            monsterDekat+=1
        #cek monster kedua di ubin4
        if(monster2X == px4 and monster2Y == py4):
            monsterDekat+=1
        #cek monster ketiga di ubin 4
        if(monster3X == px4 and monster3Y == py4):
            monsterDekat+=1
        #cek monster keempat di ubin 4
        if(monster4X == px4 and monster4Y == py4):
            monsterDekat+=1
        #cek monster kelima di ubin 4
        if(monster5X == px4 and monster5Y == py4):
            monsterDekat+=1
        #cek monster keenam di ubin 4
        if(monster6X == px4 and monster6Y == py4):
            monsterDekat+=1
        #cek monster ketujuh di ubin 4
        if(monster7X == px4 and monster7Y == py4):
            monsterDekat+=1
        #cek monster kedelapan di ubin 4
        if(monster8X == px4 and monster8Y == py4):
            monsterDekat+=1

    if(ubin5):
        #cek monster pertama di ubin5
        if(monster1X == px5 and monster1Y == py5):
            monsterDekat+=1
        #cek monster kedua di ubin5
        if(monster2X == px5 and monster2Y == py5):
            monsterDekat+=1
        #cek monster ketiga di ubin5    
        if(monster3X == px5 and monster3Y == py5):
            monsterDekat+=1
        #cek monster keempat di ubin5    
        if(monster4X == px5 and monster4Y == py5):
            monsterDekat+=1
        #cek monster klima di ubin5    
        if(monster5X == px5 and monster5Y == py5):
            monsterDekat+=1
        #cek monster keenam di ubin5    
        if(monster6X == px5 and monster6Y == py5):
            monsterDekat+=1
        #cek monster ketujuh di ubin5    
        if(monster7X == px5 and monster7Y == py5):
            monsterDekat+=1
        #cek monster kedelapan di ubin5    
        if(monster8X == px5 and monster8Y == py5):
            monsterDekat+=1
            
    if(ubin6):
        #cek monster pertama di ubin6
        if(monster1X == px6 and monster1Y == py6):
            monsterDekat+=1
        #cek monster kedua di ubin6
        if(monster2X == px6 and monster2Y == py6):
            monsterDekat+=1
        #cek monster ketiga di ubin6
        if(monster3X == px6 and monster3Y == py6):
            monsterDekat+=1
        #cek monster keempat di ubin6
        if(monster4X == px6 and monster4Y == py6):
            monsterDekat+=1
        #cek monster kelima di ubin6
        if(monster5X == px6 and monster5Y == py6):
            monsterDekat+=1
        #cek monster keenam di ubin6
        if(monster6X == px6 and monster6Y == py6):
            monsterDekat+=1
        #cek monster ketujuh di ubin6
        if(monster7X == px6 and monster7Y == py6):
            monsterDekat+=1
        #cek monster kedelapan di ubin6
        if(monster8X == px6 and monster8Y == py6):
            monsterDekat+=1
            
    if(ubin7):
        #cek monster pertama di ubin7
        if(monster1X == px7 and monster1Y == py7):
            monsterDekat+=1
        #cek monster kedua di ubin7
        if(monster2X == px7 and monster2Y == py7):
            monsterDekat+=1
        #cek monster ketiga di ubin7
        if(monster3X == px7 and monster3Y == py7):
            monsterDekat+=1
        #cek monster keempat di ubin7
        if(monster4X == px7 and monster4Y == py7):
            monsterDekat+=1
        #cek monster kelima di ubin7
        if(monster5X == px7 and monster5Y == py7):
            monsterDekat+=1
        #cek monster keenam di ubin7
        if(monster6X == px7 and monster6Y == py7):
            monsterDekat+=1
            
        #cek monster ketujuh di ubin7
        if(monster7X == px7 and monster7Y == py7):
            monsterDekat+=1
        #cek monster kedelapan di ubin7
        if(monster8X == px7 and monster8Y == py7):
            monsterDekat+=1
            
    if(ubin8):
        #cek monster pertama di ubin8
        if(monster1X == px8 and monster1Y == py8):
            monsterDekat+=1
        #cek monster kedua di ubin8
        if(monster2X == px8 and monster2Y == py8):
            monsterDekat+=1
        #cek monster ketiga di ubin8
        if(monster3X == px8 and monster3Y == py8):
            monsterDekat+=1
        #cek monster keempat di ubin8
        if(monster4X == px8 and monster4Y == py8):
            monsterDekat+=1
        #cek monster kelima di ubin8
        if(monster5X == px8 and monster5Y == py8):
            monsterDekat+=1
        #cek monster keenam di ubin8
        if(monster6X == px8 and monster6Y == py8):
            monsterDekat+=1
        #cek monster ketujuh di ubin8
        if(monster7X == px8 and monster7Y == py8):
            monsterDekat+=1
        #cek monster kedelapan di ubin8
        if(monster8X == px8 and monster8Y == py8):
            monsterDekat+=1

#cek ubin 
totalUbin=ubin1+ubin2+ubin3+ubin4+ubin5+ubin6+ubin7+ubin8
if(totalUbin == 3):
    if(monsterDekat > totalUbin-1):
        print('Senshi makannya besok aja deh.')
    else:
        print('Senshi makan hari ini!')
        
elif(totalUbin == 5):
    if(monsterDekat > totalUbin-1):
        print('Senshi makannya besok aja deh.')
    else:
        print('Senshi makan hari ini!')
        
elif(totalUbin == 8):
    if(monsterDekat > totalUbin-1):
        print('Senshi makannya besok aja deh.')
    else:
        print('Senshi makan hari ini!')
        
        
