def suma(num):
    sum = 0
    while num>0:
        sum+=num%10
        num//=10
    return sum

def multi(num):
    if num == 0:
        return 0
    mult = 1
    while num>0:
        mult*=num%10
        num//=10
    return mult


n = int(input())

odno = 0
if n == 1:
    odno == 1
count = 0
min = 0
for i in range(10**(n-1)-odno, 10**n):
    if suma(i) == multi(i):
        if count == 0:
            min = i
        count+=1
        print(count, min)
    
