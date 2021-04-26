

def IsPrime(n):
    i = 2
    while n % i != 0:
        if n ** 0.5 >= i:
            i += 1
        else:
            return n
    return i == n
