items = {
    "key": 3,
    "mace": 1,
    "gold coin": 24,
    "lantern": 1,
    "stone": 10
}

print("Equipment:")

count = 0

for item in items:
    print(items[item], item)
    count += items[item]

print(count, "items")