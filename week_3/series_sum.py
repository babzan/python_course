

n = float(input())
i = 1
s = 0.0

while n != 0:
    s = s + (1 / (n ** 2))
    n -= 1
print('{0:.6f}'.format(s))
