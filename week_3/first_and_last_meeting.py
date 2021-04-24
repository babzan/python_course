#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

s = str(input())
s1 = s.find('f')
s2 = s.rfind('f')
if s1 == s2 and s1 == -1:
    print('')
elif s1 == s2:
    print(s1)
elif s1 != s2:
    print(s1, s2)
