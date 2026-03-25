# Ada Lovelace's birthday is 10/12/1815.
# Sadly, we don't have Jack Dorsey's birthday.

d = {
    "Ada Lovelace" : "10/12/1815",
    "Jack Dorsey" : None
}

name = input()
if name in d and d[name]:
    print(name, "was born in", d[name])
else:
    print(f"sadly we don't have {name}'s birthday.")