#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

def CountSort(A):
    c = [0] * 101
    for element in A:
        c[element] += 1
    for newElement in range(101):
        print((str(newElement) + ' ') * c[newElement], end='')


n = list(map(int, input().split()))
CountSort(n)
