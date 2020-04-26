import os
from glob import glob
from collections import Counter

path = os.getcwd()
result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*'))]

f = open("allfiles.txt", "a", encoding='utf-8')
for r in result:
    print(r)
    f.write(r + "\n")
f.close()


names = []
for r in result:
    names.append(r.split('\\')[-1])
print("-------")
for i in names:
    print(i)

print("-----")
print(Counter(names))