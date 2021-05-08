#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

total_langs, all_langs = set(), set()
for i in range(int(input())):
    langs = set(input() for _ in range(int(input())))
    total_langs |= langs
    all_langs = all_langs & langs if i else langs
print(len(all_langs), '\n'.join(all_langs), sep='\n')
print(len(total_langs), '\n'.join(total_langs), sep='\n')

seq = map(int, input().split())
countDict = {}
for elem in seq:
    countDict[elem] = countDict.get(elem, 0) + 1
for key in sorted(countDict):
    print(key, countDict[key], sep=' : ')
