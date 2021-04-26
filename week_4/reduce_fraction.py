

def ReduceFraction(x, y):
    p, q = x, y
    while p != 0:
        p, q = q % p, p
    return int(x / q), int(y / q)


print(*ReduceFraction(int(input()), int(input())))
