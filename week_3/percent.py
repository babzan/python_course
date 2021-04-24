

p, x, y = float(input()), float(input()) * 100, float(input())
x = (x + y) * (100 + p) / 100
print(int(x // 100), int(x % 100))
