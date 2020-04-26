import os
from glob import glob
from collections import Counter

path = os.getcwd()
result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*'))]

sizes = {}
for r in result:
    try:
        size = os.path.getsize(r)
        sizes[r] = size
    except:
        sizes[r] = 0

sortt = {k: v for k, v in sorted(sizes.items(), key=lambda item: item[1])}

f = open("sizes.txt", "a", encoding='utf-8')
for x,y in sortt.items():
    f.write(str(y) + " - " + x + "\n")
f.close()
