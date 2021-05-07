#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

a = list(map(int, input().split()))
minVal = a.index(min(a))
maxVal = a.index(max(a))
if len(a) > 0:
    a[maxVal], a[minVal] = a[minVal], a[maxVal]
print(*a)
