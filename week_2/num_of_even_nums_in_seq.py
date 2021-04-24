#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
i = 1
number_of_evens = 0
while num != 0:
    if num % 2 == 0:
        number_of_evens = number_of_evens + 1
    num = int(input())
print(number_of_evens)
