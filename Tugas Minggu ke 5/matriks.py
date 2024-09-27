import random
a=5
b=5
matrix1=[]
matrix2=[]
matrix3=[]

#Cara 1
matrix1 = [[random.randint(0, 9) for j in range(a)] for _ in range(b)]

#cara 2
for i in range(b):
    matrix2.append([random.randint(0, 9) for j in range(a)])
    
#cara 3
for i in range(a):
    matrix3.append([])
    for j in range(b):
        matrix3[i].append(0)
        
        
        
#Parsing Matrix
h=int(input())



