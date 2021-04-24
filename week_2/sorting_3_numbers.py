#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

a, b, c = int(input()), int(input()), int(input())
if b <= a <= c:
    print(b, a, c)
elif b >= a >= c:
    print(c, a, b)
elif a <= b <= c:
    print(a, b, c)
elif a >= b >= c:
    print(c, b, a)
elif a <= c <= b:
    print(a, c, b)
elif a >= c >= b:
    print(b, c, a)
