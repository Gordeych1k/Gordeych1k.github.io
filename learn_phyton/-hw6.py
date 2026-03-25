names = ("Aaaa   ", "BBBBBB ", "              cccccc                  ")
result = list(map(lambda name: name.strip().capitalize(), names))
print(result) 