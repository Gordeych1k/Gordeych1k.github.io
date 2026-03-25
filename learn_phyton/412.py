numbers = list(map(int, input().split()))
n = int(input())

for i in numbers:
    if n > i:
        print(i)