#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
minutes = num % 60
hours = num // 60 % 24
print(hours, minutes, end='')