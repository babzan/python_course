#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
if num % 10 == 1 and num != 11:
    print(num, "korova", end='')
elif (num % 10 == 2 and num != 12) or (num % 10 == 3 and num != 13) or \
        (num % 10 == 4 and num != 14):
    print(num, "korovy", end='')
else:
    print(num, "korov", end='')
