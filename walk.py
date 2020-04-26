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
sortt = {k: v for k, v in sorted(say.items(), key=lambda item: item[1])}


f = open("counter.txt", "a", encoding='utf-8')
for x,y in sortt.items():
    f.write(x + " - " + str(y) + "\n")
f.close()
