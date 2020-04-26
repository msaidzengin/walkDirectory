import os
from glob import glob
from collections import Counter

path = os.getcwd()
result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*'))]

f = open("allfiles.txt", "a", encoding='utf-8')
for r in result:
    f.write(r + "\n")
f.close()


names = []
for r in result:
    names.append(r.split('\\')[-1])

say = Counter(names)

f = open("counter.txt", "a", encoding='utf-8')
for x,y in say.items():
    f.write(x + " - " + str(y) + "\n")
f.close()
