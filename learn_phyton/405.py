# a = list(map(int, input().split()))
# print(*a[len(a)//2:])

a = list(map(int, input().split()))
l = len(a)//2
print(*a[l:])
