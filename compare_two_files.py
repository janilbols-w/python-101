import os
import filecmp

f1 = './a.txt'
f2 = './b.txt'
print(filecmp.cmp(r'{}'.format(f1),r'{}'.format(f2)))
