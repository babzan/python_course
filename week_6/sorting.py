#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

number_of_elements = int(input())
unsorted_list = list(map(int, input().split()))
unsorted_list.sort(reverse=False)
print(*unsorted_list)
