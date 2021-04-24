#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

first = int(input())
last = int(input())
comparison = last / (last - first + 1)
if first <= last and comparison % 1 == 0:
    if last % comparison == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
