#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

a = int(input())
b, c, d = 0, a, 0
while a != 0:
    if a == c:
        b += 1
        if b > d:
            d = b
    else:
        c = a
        b = 1
    a = int(input())
print(d)
