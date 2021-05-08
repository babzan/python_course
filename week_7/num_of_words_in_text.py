#################################
#                               #
#       BABAK HUSEYNOV          #
#                               #
#################################

# For test it you'll need use this command at command
# line in UNIX-like systems:
# cat text_file.txt | python3 python.py

import sys
print(len(set(sys.stdin.read().split())))
