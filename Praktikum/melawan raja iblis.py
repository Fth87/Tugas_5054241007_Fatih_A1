HPUcup = int(input())
Knight = int(input())
Minion = int(input())

APUcup = 100


HPMinion = 100
MinionBeku=Minion//2
APMinion = 2 * MinionBeku * (HPMinion / APUcup)


HPKnight = 500
KnightBeku=Knight//2
APKnight = 5 * KnightBeku * (HPKnight / APUcup)

HPRaja = 1000
APRaja = 100 * (HPRaja / APUcup)


totalSerangan = APMinion+APKnight+APRaja
HPUcup-=totalSerangan


if(HPUcup>=0):
    print(f'Yey! Ucup Menang! HP tersisa : {round(HPUcup)}')    
else:
    print('Yah! Ucup Meninggoy.')
