words = input().split()
res = ''.join(word[-1] for word in words)
print(res)
