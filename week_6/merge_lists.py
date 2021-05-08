#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

def merge(list1, list2):
    i, j = 0, 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    res += list1[i:]
    res += list2[j:]
    return res


a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
print(*merge(a1, a2))
