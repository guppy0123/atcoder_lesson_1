n,m,l=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
B=[list(map(int,input().split())) for i in range(m)]

C=[]
for i in range(n):
    line=[]
    for j in range(l):
        c=0
        for k in range(m):
            c+=A[i][k]*B[k][j]
        line.append(c)
    C.append(line)

for line in C:
    print(*line)