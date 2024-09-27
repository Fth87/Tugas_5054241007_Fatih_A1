N,K = map(int,input().split())
A = list(map(int,input().split()))

temp=0
for i in range(N):
    if A[i] >= K:
      temp+=1
print(temp)