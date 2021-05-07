#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

a = list(map(int, input().split()))
maxVal, j = a[0], 0
for i in range(len(a)):
    if a[i] >= maxVal:
        maxVal = a[i]
        j = i
print(maxVal, j)
