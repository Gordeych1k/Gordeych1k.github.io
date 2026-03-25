matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
for i in matrix:
     sum_row = sum(i)
     print(sum_row)
print("----------")

s=0
s1=0
s2=0
for i in matrix:
     for j in i:
        s+=i[0]
print(s)


for i in matrix:
     for j in i:
          if j == 0:
            print("True")