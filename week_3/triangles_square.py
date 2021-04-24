#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

n1 = float(input())
n2 = float(input())
n3 = float(input())
epsilon = 10 ** -6

semi = (n1 + n2 + n3) / 2
square = (semi * (semi - n1) * (semi - n2) * (semi - n3))**0.5

if abs(int(square) - float(square)) < epsilon:
    print(int(square))
else:
    print("{0:.6f}".format(square))
