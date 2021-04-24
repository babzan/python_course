#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
i = 1
maxNum = num
while num != 0:
    num = int(input())
    if maxNum < num:
        maxNum, num = num, maxNum
print(maxNum)
