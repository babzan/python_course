

def sumOfS(x):
    x = int(input())
    if x == 0:
        return 0
    return x + sumOfS(x)


x = 0
print(sumOfS(x))
