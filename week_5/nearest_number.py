#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

n = int(input())
a = list(map(int, input().split()))
b = []
i = 0
num = int(input())
while i < n:
    b.insert(i, a[i] - num)
    i += 1
    minIn = b.index(min(b, key=abs))
print(a[minIn])
