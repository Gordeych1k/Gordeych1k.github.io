numbers = list(map(int, input().split()))
result = list(filter(lambda x: x % 2 == 0 and x > 10, numbers))
print(result)