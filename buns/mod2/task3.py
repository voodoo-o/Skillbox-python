a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if (a >= b and a <= c) or (a <= b and a >= c):
    print(a)
elif (b <= a and b >= c) or (b <= c and b >= a):
    print(b)
elif (c <= b and c >= a) or (c <= a and a >= b):
    print(c)
