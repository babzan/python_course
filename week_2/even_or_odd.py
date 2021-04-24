#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n1 % 2 == 0 and n2 % 2 != 0 or n3 % 2 != 0) or \
        (n2 % 2 == 0 and n1 % 2 != 0 or n3 % 2 != 0) or \
        (n3 % 2 == 0 and n2 % 2 != 0 or n1 % 2 != 0):
    print('YES')
else:
    print('NO')
