text = input()
dct = {i: text.count(i) for i in text}
# for i in text:
#     n = text.count(i)
#     dct[i] = n

print(dct)