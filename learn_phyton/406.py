text = list(map(int,input().split()))
last = text[-1]
forlast = text[-2]

newlist = text[:-2]

print(forlast,last,*newlist)