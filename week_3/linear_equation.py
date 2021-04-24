

a, b, c, d, e, f = float(input()), float(input()), float(input()),\
                   float(input()), float(input()), float(input())
if a != 0 and b != 0 and c != 0 and d != 0:
    y = (a*f-c*e)/(a*d-c*b)
    x = (e-b*y)/a
    print('{0:.6f}'.format(x), '{0:.6f}'.format(y))
elif a == 0 and b != 0 and c != 0 and d == 0:
    y = e/b
    x = f/c
    print('{0:.6f}'.format(x), '{0:.6f}'.format(y))
elif a != 0 and b == 0 and c == 0 and d != 0:
    y = f/d
    x = e/a
    print('{0:.6f}'.format(x), '{0:.6f}'.format(y))
