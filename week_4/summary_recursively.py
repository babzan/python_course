

def summary(a, b):
    i = 0
    if a == 0:
        return b
    if b == 0:
        return a
    if a > 0:
        i += 1
        return i + (summary(a, b - 1))


a, b = int(input()), int(input())
print(summary(a, b))
