import os
from glob import glob
from collections import Counter

path = os.getcwd()
result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*'))]

sizes = {}
for r in result:
    size = os.path.getsize(r)
    sizes[r] = size

sortt = {k: v for k, v in sorted(sizes.items(), key=lambda item: item[1])}

f = open("sizes.txt", "a", encoding='utf-8')
for x,y in sortt.items():
    f.write(x + " - " + str(y) + "\n")
f.close()
