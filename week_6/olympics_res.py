#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

count = int(input())
members = []
for i in range(count):
    members.append(list(input().split()))
members.sort(key=lambda ls: int(ls[1]), reverse=True)
for member in members:
    print(member[0])
