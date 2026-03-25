m, n, k = map(int, input().split())

count = len(str(m/n - int(m/n)))-2
if count<k: