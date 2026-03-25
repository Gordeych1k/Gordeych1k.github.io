def stalin_sort(numbers):
    i = 1
    l = len(numbers)
    while not l == 0:
        if numbers[i]<numbers[i-1]:
            numbers.remove(numbers[i])
        else:
            i+=1
        l -= 1
    return numbers

print(stalin_sort([1, 2, 3, 4, 5]))
# print(stalin_sort([5, 3, 1, 2, 4] ))
# print(stalin_sort([1, 2, 2, 3, 1, 4] ))
# print(stalin_sort([3, 1, 4, 1, 5, 9, 2]))
# print(stalin_sort([] ))

