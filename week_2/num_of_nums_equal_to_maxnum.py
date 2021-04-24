#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
numbers_of = 0
maxNum = num
while num != 0:
    if maxNum == num:
        numbers_of = numbers_of + 1
    elif maxNum < num:
        maxNum, num = num, maxNum
        numbers_of = 1
    num = int(input())
print(numbers_of)
