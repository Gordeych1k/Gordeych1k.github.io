n = int(input())
for i in range(10, 100):
    if ((i//10)**2 + (i%10)**2)%n == 0:
        print(i)