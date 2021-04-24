#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

s = str(input())
h = 'h'
s1 = s.find(h)
s2 = s.rfind(h)
print(s[:s1], s[s2 + 1:], sep='')
