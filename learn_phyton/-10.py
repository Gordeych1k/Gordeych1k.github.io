n = int(input())
s=0
for i in range(n, 0, -1):
    s+=1/i
    if s>0.5:
        break
print(i)