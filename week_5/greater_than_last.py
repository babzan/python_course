#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

a = list(map(int, input().split()))
maxVal = a[0]
b = a[0]
for i in range(len(a)):
    if b < a[i]:
        print(a[i], end=' ')
    b = a[i]
