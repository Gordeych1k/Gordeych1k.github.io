numbers = [1, 2, 3, 4, -1, -19, 0]
# result = sum(filter(lambda n: n>0, numbers))
# print(result)

result = sum(n for n in numbers if n>0)
print(result)