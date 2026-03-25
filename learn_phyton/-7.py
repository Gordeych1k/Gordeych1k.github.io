matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = []

for matris in matrix:
    new_matris = list(map(lambda i: i*2, matris))
    new_matrix.append(new_matris)
print(new_matrix)

# for i in matrix:
#     for j in i:
#         if j>8:
#             print("True")
#             break
    

# for i in matrix:
#     for j in i:
#        s+=j
# print(s) 
# suma = sum(map(lambda list: sum(list), matrix))                                                     