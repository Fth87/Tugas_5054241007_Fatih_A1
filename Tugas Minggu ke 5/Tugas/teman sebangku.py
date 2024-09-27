N,r,c=map(int,input().split())
# r = baris, c = kolom
# A = banyak murid
A = [list(map(int,input().split())) for _ in range(N)]

#perulangan untuk mencari teman yang sebelahan
for i in range(N):
#temp = untuk menyimpan teman sebangku yang sebelahan per baris
  temp=[]*N
  for j in range(N):
#untuk mengecek apakah ada teman sebangku yang sebelahan dengan cara membandingkan apakah ada kolom yang sama dan orangnua tidak sama
    if(A[i][1] == A[j][1] and A[i][0] != A[j][0]):
      temp.append(A[j][0])
  if len(temp) > 0:
    for k in range(len(temp)):
      print(temp[k])
  else:
    print(0)
#temp direset untuk baris selanjutnya
  temp=[]*N  

  
print("Matrix A: " + str(A))
