n = int(input())
k=0
for j in range (1,n+1):
    m = 1
    for i in range(1,j+1):
        m*=i
    k+=m
print(k)

