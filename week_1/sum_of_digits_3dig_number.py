#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
summary = (num % 10) + (num // 100) + (num // 10 % 10)
print(summary, end='')