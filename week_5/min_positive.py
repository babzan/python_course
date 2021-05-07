#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

arr = list(map(int, input().split()))
arr2 = []
for i in range(len(arr)):
    if arr[i] > 0:
        arr2.append(arr[i])
    else:
        continue
print(min(arr2))
