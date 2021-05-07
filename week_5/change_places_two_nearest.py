#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

a = list(map(int, input().split()))
if len(a) % 2 == 1:
    n = len(a) - 2
else:
    n = len(a) - 1
i = 0
while i < n:
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 2
print(*a)
