import os
from glob import glob
path = os.getcwd()
result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.txt'))]

f = open("allfiles.txt", "a", encoding='utf-8')
for r in result:
    print(r)
    f.write(r + "\n")
f.close()
