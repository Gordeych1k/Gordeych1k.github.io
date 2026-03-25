text = input()
LOWER = 0
UPPER = 0
for i in text:
    if i.islower():
        LOWER+=1
    elif i.isupper():
        UPPER+=1
print("LOWER", LOWER, "UPPER", UPPER)