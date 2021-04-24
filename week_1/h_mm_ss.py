#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

start_seconds = int(input())
hours = start_seconds // 3600 % 24
minutes = str(start_seconds // 60 % 60 // 10) + str(start_seconds // 60 % 10)
seconds = str(start_seconds % 60 // 10) + str(start_seconds % 1000 % 10)
print(hours, ":", minutes, ':', seconds, sep='', end='')