users = {
    232: "Alice",
    550: "Bob",
    190: "Jack"
}

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in [a, b, c, d]:
    if i in users:
        print("Hi,", users[i] + "!")
    else:
        print("Hi, to all!")
