N,r,c=map(int,input().split())
# r = baris, c = kolom
# A = banyak murid
A = [list(map(int,input().split())) for _ in range(N)]
kursi = [[0 for _ in range(c)] for _ in range(r)]

#Untuk menjadikan matriks orang yang ada di kursi
for i in range(len(A)):
  kursi[A[i][1]-1][A[i][2]-1] += 1
  
#Menghitung jumlah orang yang ada di kursi per baris
for i in range(len(kursi)):
  temp = 0
  for j in range(c):
    temp += kursi[i][j]
  temp = 0
  
  
print("Matrix A: " + str(A))
print("Matrix Kursi: " + str(kursi))