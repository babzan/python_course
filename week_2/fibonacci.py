#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

num = int(input())
s1 = 0
s2 = 1
i = 0
while i < num:
    s3 = s1 + s2
    s1 = s2
    s2 = s3
    i = i + 1
print(s1)
