#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
maxNum = 0
secNum = 0
while num != 0:
    if maxNum <= num:
        secNum = maxNum
        maxNum = num
    elif secNum <= num:
        secNum = num
    num = int(input())
print(secNum)
