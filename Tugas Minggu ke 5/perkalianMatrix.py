# Get dimensions for matrix A
baris_matrix1 = int(input("Enter the number of rows for matrix A: "))
kolom_matrik1 = int(input("Enter the number of columns for matrix A: "))

# Get dimensions for matrix B
baris_matrix2 = int(input("Enter the number of rows for matrix B: "))
kolom_matrix2 = int(input("Enter the number of columns for matrix B: "))

# Ensure the matrices can be multiplied
if kolom_matrik1 != baris_matrix2:
  print("Number of columns in A must be equal to number of rows in B")
  exit()
  
matrix1 = [list(map(int,input().split())) for _ in range(baris_matrix1)]
matrix2 = [list(map(int,input().split())) for _ in range(baris_matrix2)]

#Kalikan kedua matriks

result = [[0 for j in range(kolom_matrix2)] for i in range(baris_matrix1)]
for i in range(baris_matrix1):
  for j in range(kolom_matrix2):
    for k in range(kolom_matrik1):
      result[i][j] += matrix1[i][k] * matrix2[k][j]

  
print("Matrix A: " + str(matrix1))
print("Matrix B: " + str(matrix2))
print("Hasil : " + str(result))



