#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

set_1 = list(map(int, input().split()))
set_2 = set()

for i in range(len(set_1)):
    if set_1[i] not in set_2:
        set_2.add(set_1[i])
        print('NO')
    else:
        print('YES')
