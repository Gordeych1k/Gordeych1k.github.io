numbers = list(map(int, input().split()))

smallest = min(numbers)
biggest = max(numbers)

index_smallest = numbers.index(smallest)
index_biggest = numbers.index(biggest)

numbers[index_smallest] = biggest
numbers[index_biggest] = smallest

print(*numbers)



